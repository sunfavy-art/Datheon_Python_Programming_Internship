import csv
# Datheon Python Programming Internship
# Task 1: Investment Portfolio Tracker

# Store portfolio information
portfolio = {}

print("===================================")
print("     INVESTMENT PORTFOLIO TRACKER")
print("===================================")

print("Welcome to your investment tracker!")
# Ask the user how many stocks they want to enter
number_of_stocks = int(input("\nHow many stocks do you want to add? "))

# Collect stock information
for i in range(number_of_stocks):

    print(f"\nStock {i + 1}")

    ticker = input("Enter stock ticker (e.g. AAPL): ").upper()

    buy_price = float(input("Enter purchase price: "))

    quantity = int(input("Enter number of shares: "))

    # Store the information
    portfolio[ticker] = {
        "buy_price": buy_price,
        "quantity": quantity
    }

print("\nYour portfolio information has been saved!")
print(portfolio)
# Calculate total invested capital
total_invested = 0

for ticker, details in portfolio.items():

    investment = details["buy_price"] * details["quantity"]

    total_invested += investment

    print(f"\n{ticker}")
    print(f"Purchase Price: ${details['buy_price']}")
    print(f"Quantity: {details['quantity']}")
    print(f"Total Investment: ${investment:.2f}")

print("\n===================================")
print(f"TOTAL INVESTED: ${total_invested:.2f}")
print("===================================")
# Calculate current portfolio value
total_current_value = 0
portfolio_summary = []

for ticker, details in portfolio.items():

    current_price = float(input(
        f"\nEnter current market price for {ticker}: $"
    ))

    buy_price = details["buy_price"]
    quantity = details["quantity"]

    invested = buy_price * quantity
    current_value = current_price * quantity

    profit_loss = current_value - invested

    if invested > 0:
        percentage = (profit_loss / invested) * 100
    else:
        percentage = 0

    total_current_value += current_value

    portfolio_summary.append({
        "Ticker": ticker,
        "Buy Price": buy_price,
        "Quantity": quantity,
        "Current Price": current_price,
        "Invested": invested,
        "Current Value": current_value,
        "Profit/Loss": profit_loss,
        "Percentage": percentage
    })
    print(f"\n--- {ticker} RESULTS ---")
    print(f"Invested: ${invested:.2f}")
    print(f"Current Value: ${current_value:.2f}")
    print(f"Profit/Loss: ${profit_loss:.2f}")
    print(f"Percentage: {percentage:.2f}%")

print("\n==============================")
print(f"Total Invested: ${total_invested:.2f}")
print(f"Current Value: ${total_current_value:.2f}")
print(f"Overall Profit/Loss: ${total_current_value - total_invested:.2f}")
print("==============================")
# Save portfolio results to CSV
with open("portfolio_summary.csv", "w", newline="") as file:

    fieldnames = [
        "Ticker",
        "Buy Price",
        "Quantity",
        "Current Price",
        "Invested",
        "Current Value",
        "Profit/Loss",
        "Percentage"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerows(portfolio_summary)

print("\nPortfolio summary successfully saved!")