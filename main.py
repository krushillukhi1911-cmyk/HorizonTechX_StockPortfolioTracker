import sys
from services.portfolio_service import PortfolioService
from services.analytics_service import AnalyticsService
from services.report_service import ReportService
from config.stock_prices import stocks

def display_menu():
    print("\n=================================================")
    print("STOCK PORTFOLIO TRACKER")
    print("=================================================")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Search Stock")
    print("4. Update Stock")
    print("5. Delete Stock")
    print("6. Portfolio Analytics")
    print("7. Generate Report")
    print("8. Exit")
    print("=================================================")

def main():
    portfolio_service = PortfolioService()
    
    while True:
        display_menu()
        try:
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == '1':
                print("\nAvailable Stocks:", ", ".join(stocks.keys()))
                symbol = input("Enter Stock Symbol: ").strip()
                quantity_str = input("Enter Quantity: ").strip()
                if not quantity_str.isdigit():
                    print("Error: Invalid Quantity. Please enter a valid number.")
                    continue
                quantity = int(quantity_str)
                portfolio_service.add_stock(symbol, quantity)
                
            elif choice == '2':
                portfolio_service.view_portfolio()
                
            elif choice == '3':
                symbol = input("Enter Stock Symbol to search: ").strip()
                portfolio_service.search_stock(symbol)
                
            elif choice == '4':
                symbol = input("Enter Stock Symbol to update: ").strip()
                quantity_str = input("Enter new Quantity: ").strip()
                if not quantity_str.isdigit():
                    print("Error: Invalid Quantity. Please enter a valid number.")
                    continue
                quantity = int(quantity_str)
                portfolio_service.update_stock(symbol, quantity)
                
            elif choice == '5':
                symbol = input("Enter Stock Symbol to delete: ").strip()
                portfolio_service.delete_stock(symbol)
                
            elif choice == '6':
                AnalyticsService.display_analytics(portfolio_service)
                
            elif choice == '7':
                ReportService.generate_report(portfolio_service)
                
            elif choice == '8':
                print("Exiting Stock Portfolio Tracker. Goodbye!")
                sys.exit(0)
                
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
                
        except KeyboardInterrupt:
            print("\nExiting Stock Portfolio Tracker. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
