#stock price (dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "MSFT": 320,
    "AMZN": 170
}

#display available stocks
print("="*40)
print(" STOCK PORTFOLIO TRACKER")
print("="*40)
print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

#stored portfolio data
portfolio = []
total_investment = 0

#take stock input from user
print("\n--- Add Stocks to Your Portfolio ---")

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper().strip()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print(f" '{stock_name}' not found! Please choose from the list above.")
        continue
    try:
        quantity = int(input(f" How many shares of {stock_name}?"))
        if quantity <= 0:
            print(" Quantity must be a positive number!")
            continue
    except ValueError:
        print("Please enter a valid number!")
        continue
#Calculate investment

    price = stock_prices[stock_name]
    investment = price*quantity
    total_investment += investment

    portfolio.append({
        "stock": stock_name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

    print(f" Added! {quantity} x${price} = ${investment}")

#display summary
if not portfolio:
    print("\nNo stocks were added to the portfolio.")
else:
    print("\n"+ "="*40)
    print(" PORTFOLIO SUMMARY")
    print("="*40)
    print("{stock: <8} {'Qty': <6} {'price': <8} {'value'}")
    print("-"*40)
    for item in portfolio:
        print(f"{item['stock']: <8} {item['quantity']: <6} ${item['price']: <7} ${item['investment']}")
    print("-"*40)
    print(f" TOTAL INSVESTMENT --> ${total_investment}")
    print("="*40)

#save to file
save = input("\nDo you want to save the result? (yes/no):")

if save == "yes":
    choice = input("Choose format (txt/csv):").lower()
    
    if choice == "txt":
        with open("portfolio_result.txt", "w") as f:
            f.write("STOCK PORTFOLIO SUMMARY\n")
            f.write("="*40 + "\n")
            for item in portfolio:
                f.write(f"{item['stock']}: {item['quantity']} shares x ${item['price']} = ${item['investment']}\n")
            f.write("-"*40 + "\n")
            f.write(f"TOTAL: ${total_investment}\n")
            print("Saved -=> portfolio_result.txt")

    elif choice =="csv":
        with open("portfolio_result.csv", "w") as f:
            f.write("Stock,Quantity,Price,Investment\n")
            for item in portfolio:
                f.write(f"{item['stock']}, {item['quantity']}, {item['price']}, {item['investment']}\n")
            f.write(f"TOTAL,,,{total_investment}\n")
            print("Saved --> portfolio_result.csv")

print("\nThank you for using Stock Portfolio Tracker!")