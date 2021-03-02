import dataScrape as d
import analysis as a
import robin_stocks as r

d.login()

ticker = "BTC"

over = False

owned = False

amountInUSD = 100

amountInAsset = round(amountInUSD / d.price(ticker), 5)

unitsOwned = 0

averagePrice = 0

totalOwned = 0

while not over:
    command = input("Enter command: ")

    price = d.price(ticker)
    
    if (command == "quit"):
        over = True
    
    if (command == "auto"):
        reccomendation = a.strat(verbose = False)
        if (reccomendation == 1):
            command = "BUY"
        else:
            command = "SELL"
    
    if (command == "price"):
        print("Price: $" + str(price))
        print("Total Owned: $" + str(totalOwned))
        if (owned):
            profit = (a.percentDiff(price, averagePrice) / 100) * amountInUSD
            print("Profit: $" + str(profit))
    
    if (command == "show"):
        data = d.dataPoints(ticker, 0, 1)
        a.showIndicators(data)
        reccomendation = a.strat(verbose = False)
        if reccomendation == 1:
            print("Reccomended action: BUY")
        else:
            print("Reccomended action: SELL")
    
    if (command == "BUY"):
        r.order_buy_crypto_by_price(ticker, amountInUSD)
        print("Bought at $" + str(price))
        owned = True
        totalOwned += price
        unitsOwned += 1
        averagePrice = totalOwned / unitsOwned

    if (command == "SELL"):
        r.order_sell_crypto_by_price(ticker, amountInUSD*unitsOwned)
        print("Sold at $" + str(price))
        owned = False
        averagePrice = 0
        unitsOwned = 0
        totalOwned = 0
    
    print('\n')
    
