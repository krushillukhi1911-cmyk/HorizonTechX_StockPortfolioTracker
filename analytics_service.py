import logging

class AnalyticsService:
    @staticmethod
    def display_analytics(portfolio_service):
        try:
            portfolio = portfolio_service.portfolio
            if not portfolio:
                print("\nPortfolio is empty. No analytics to display.")
                return

            total_stocks_owned = len(portfolio)
            highest_investment = max(portfolio, key=lambda s: s.investment_value)
            lowest_investment = min(portfolio, key=lambda s: s.investment_value)
            total_value = sum(s.investment_value for s in portfolio)
            average_investment = total_value / total_stocks_owned if total_stocks_owned > 0 else 0

            print("\n=====================================")
            print("PORTFOLIO SUMMARY")
            print("=====================================")
            print(f"Total Stocks Owned: {total_stocks_owned}\n")
            print("Highest Investment:")
            print(f"{highest_investment.stock_symbol} = ${highest_investment.investment_value}\n")
            print("Lowest Investment:")
            print(f"{lowest_investment.stock_symbol} = ${lowest_investment.investment_value}\n")
            print("Average Investment:")
            print(f"${average_investment:.2f}\n")
            print("Total Portfolio Value:")
            print(f"${total_value}\n")
            print("=====================================")
            logging.info("Analytics Displayed")

        except Exception as e:
            logging.error(f"Error displaying analytics: {e}")
            print(f"An error occurred: {e}")
