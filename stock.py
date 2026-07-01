import datetime

class Stock:
    def __init__(self, stock_symbol, stock_name, quantity, price):
        self.stock_symbol = stock_symbol.upper()
        self.stock_name = stock_name
        self.quantity = int(quantity)
        self.price = float(price)
        self.investment_value = self.calculate_value()
        self.created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def calculate_value(self):
        return self.quantity * self.price

    def display_stock(self):
        print(f"Symbol: {self.stock_symbol}")
        print(f"Name: {self.stock_name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: {self.price}")
        print(f"Investment Value: {self.investment_value}")
        print(f"Created Date: {self.created_date}")

    def to_dict(self):
        return {
            "symbol": self.stock_symbol,
            "name": self.stock_name,
            "quantity": self.quantity,
            "price": self.price,
            "value": self.investment_value,
            "created_date": self.created_date
        }
