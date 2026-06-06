stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 320
}

total_investment = 0

print("=== STOCK PORTFOLIO TRACKER ===")

n = int(input("How many stocks do you want to enter? "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment
    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total_investment)

# Optional file saving
file = open("portfolio.txt", "w")
file.write("Total Investment Value = " + str(total_investment))
file.close()

print("Result saved in portfolio.txt")