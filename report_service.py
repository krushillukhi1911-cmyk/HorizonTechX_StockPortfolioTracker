import csv
import os
import datetime
import logging

class ReportService:
    @staticmethod
    def generate_report(portfolio_service, report_file="reports/investment_report.csv"):
        try:
            os.makedirs("reports", exist_ok=True)
            portfolio = portfolio_service.portfolio
            
            if not portfolio:
                print("\nPortfolio is empty. Cannot generate report.")
                return

            with open(report_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Stock Symbol", "Quantity", "Price", "Investment Value"])
                
                current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                for stock in portfolio:
                    writer.writerow([
                        current_date, 
                        stock.stock_symbol, 
                        stock.quantity, 
                        stock.price, 
                        stock.investment_value
                    ])
            
            print(f"\nReport Generated successfully at {report_file}")
            logging.info("Report Generated")
        except Exception as e:
            logging.error(f"Error generating CSV report: {e}")
            print(f"An error occurred while generating report: {e}")
