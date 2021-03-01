import dataScrape as d
import analysis as a
import robin_stocks as r

d.login()

ticker = "BTC"

over = False

owned = False

amountInUSD = 100

amountInAsset = round(100 / d.price(ticker), 6)

while not over:
    command = input("Enter command: ")

    price = d.price(ticker)

    if (owned):
        profit = (a.percentDiff(price, purchasePrice) / 100)* amountInUSD
        print("Profit: $" + str(profit))
    
    if (command == "quit"):
        over = True
    
    if (command == "price"):
        print(price)
    
    if (command == "show"):
        data = d.dataPoints(ticker, 0, 1)
        a.showIndicators(data)
        reccomendation = a.strat(verbose = False)
        print("Reccomended action: " + str(reccomendation))
    
    if (command == "BUY"):
        #r.order_buy_crypto_by_price(ticker, amountInUSD)
        purchasePrice = d.price(ticker)
        amountInAsset = 100 / purchasePrice
        print("Bought at $" + str(purchasePrice))
        owned = True

    if (command == "SELL"):
        print(amountInAsset)
        r.order_sell_crypto_by_quantity(ticker, amountInAsset)
        price = price
        print("Sold at $" + str(price))
        owned = False
    
