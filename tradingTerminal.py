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

while not over:
    command = input("Enter command: ")

    price = d.price(ticker)
    
    if (command == "quit"):
        over = True
    
    if (command == "price"):
        print("Price of : $" + str(price))

        if (owned):
            profit = (a.percentDiff(price, averagePrice) / 100)* amountInUSD
            print("Profit: $" + str(profit))
    
    if (command == "show"):
        data = d.dataPoints(ticker, 0, 1)
        a.showIndicators(data)
        reccomendation = a.strat(verbose = False)
        if reccomendation == 1:
            print("Reccomended action: BUY")
        else:
            print("Reccomended action: SELL")
    if (command == "remind"):
        sleep(300)
    
    if (command == "BUY"):
        r.order_buy_crypto_by_price(ticker, amountInUSD)
        unitsOwned += 1
        averagePrice += price
        averagePrice /= unitsOwned
        amountInAsset += round(amountInUSD / price, 5)
        print("Bought at $" + str(price))
        owned = True

    if (command == "SELL"):
        if (unitsOwned == 0):
            unitsOwned = 1
        r.order_sell_crypto_by_quantity(ticker, amountInAsset*unitsOwned)
        print("Sold at $" + str(price))
        owned = False
        averagePrice = 0
        unitsOwned = 0
    
    print('\n')
    
