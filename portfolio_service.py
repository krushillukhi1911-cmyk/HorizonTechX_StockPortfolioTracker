import json
import os
import logging
from models.stock import Stock
from config.stock_prices import stocks

# Setup Logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/portfolio.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class PortfolioService:
    def __init__(self, data_file="data/portfolio.json"):
        self.data_file = data_file
        self.portfolio = []
        os.makedirs("data", exist_ok=True)
        self.load_portfolio()

    def load_portfolio(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    for item in data:
                        stock = Stock(item['symbol'], item.get('name', ''), item['quantity'], item['price'])
                        stock.investment_value = item['value']
                        stock.created_date = item.get('created_date', stock.created_date)
                        self.portfolio.append(stock)
                logging.info("Portfolio loaded successfully")
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from portfolio file")
            print("Error: Could not load data. The portfolio file might be corrupted.")
        except Exception as e:
            logging.error(f"Error loading portfolio: {e}")
            print(f"An unexpected error occurred: {e}")

    def save_portfolio(self):
        try:
            with open(self.data_file, 'w') as file:
                json.dump([stock.to_dict() for stock in self.portfolio], file, indent=4)
            logging.info("Portfolio saved successfully")
        except Exception as e:
            logging.error(f"Error saving portfolio: {e}")
            print(f"Error: Could not save data. {e}")

    def add_stock(self, symbol, quantity):
        try:
            symbol = symbol.upper()
            if symbol not in stocks:
                print("Error: Invalid Symbol. Stock not found in predefined prices.")
                logging.warning(f"Failed to add stock. Invalid symbol: {symbol}")
                return

            if not isinstance(quantity, int) or quantity <= 0:
                print("Error: Invalid Quantity. Must be a positive integer.")
                logging.warning(f"Failed to add stock. Invalid quantity: {quantity}")
                return

            price = stocks[symbol]
            name = symbol # Assuming name is symbol for simplicity, or could fetch from a dict
            
            # Check if stock already exists in portfolio to update quantity instead
            for stock in self.portfolio:
                if stock.stock_symbol == symbol:
                    stock.quantity += quantity
                    stock.investment_value = stock.calculate_value()
                    self.save_portfolio()
                    print("\nStock Added Successfully (Updated existing)")
                    stock.display_stock()
                    logging.info("Stock Added (Updated)")
                    return

            new_stock = Stock(symbol, name, quantity, price)
            self.portfolio.append(new_stock)
            self.save_portfolio()
            
            print("\nStock Added Successfully")
            new_stock.display_stock()
            logging.info("Stock Added")
            
        except Exception as e:
            logging.error(f"Error adding stock: {e}")
            print(f"An error occurred: {e}")

    def view_portfolio(self):
        try:
            if not self.portfolio:
                print("\nPortfolio is empty.")
                return

            print("\n---------------------------------------------------------")
            print(f"{'SYMBOL':<10} {'QTY':<10} {'PRICE':<10} {'VALUE':<10}")
            print("---------------------------------------------------------")
            
            total_value = 0
            for stock in self.portfolio:
                print(f"{stock.stock_symbol:<10} {stock.quantity:<10} {stock.price:<10} {stock.investment_value:<10}")
                total_value += stock.investment_value
                
            print("---------------------------------------------------------")
            print(f"TOTAL VALUE = {total_value}")
            print("---------------------------------------------------------")
            logging.info("Viewed Portfolio")
        except Exception as e:
            logging.error(f"Error viewing portfolio: {e}")
            print(f"An error occurred: {e}")

    def search_stock(self, symbol):
        try:
            symbol = symbol.upper()
            for stock in self.portfolio:
                if stock.stock_symbol == symbol:
                    print("\nStock Found")
                    stock.display_stock()
                    logging.info(f"Searched for stock: {symbol} - Found")
                    return stock
            
            print(f"\nStock {symbol} not found in your portfolio.")
            logging.info(f"Searched for stock: {symbol} - Not Found")
            return None
        except Exception as e:
            logging.error(f"Error searching stock: {e}")
            print(f"An error occurred: {e}")

    def update_stock(self, symbol, new_quantity):
        try:
            symbol = symbol.upper()
            if not isinstance(new_quantity, int) or new_quantity < 0:
                print("Error: Invalid Quantity. Must be a non-negative integer.")
                return

            for stock in self.portfolio:
                if stock.stock_symbol == symbol:
                    if new_quantity == 0:
                        self.delete_stock(symbol)
                        return
                    
                    stock.quantity = new_quantity
                    stock.investment_value = stock.calculate_value()
                    self.save_portfolio()
                    print("\nStock Updated Successfully")
                    stock.display_stock()
                    logging.info("Stock Updated")
                    return
            
            print(f"\nStock {symbol} not found in your portfolio.")
        except Exception as e:
            logging.error(f"Error updating stock: {e}")
            print(f"An error occurred: {e}")

    def delete_stock(self, symbol):
        try:
            symbol = symbol.upper()
            for i, stock in enumerate(self.portfolio):
                if stock.stock_symbol == symbol:
                    del self.portfolio[i]
                    self.save_portfolio()
                    print("\nStock Deleted Successfully")
                    logging.info("Stock Deleted")
                    return
            
            print(f"\nStock {symbol} not found in your portfolio.")
        except Exception as e:
            logging.error(f"Error deleting stock: {e}")
            print(f"An error occurred: {e}")

