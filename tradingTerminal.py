import dataScrape as d
import analysis as a
import robin_stocks as r
from time import sleep

d.login()

ticker = "BTC"

over = False

owned = False

amountInUSD = 100

amountInAsset = round(amountInUSD / d.price(ticker), 5)

unitsOwned = 0

averagePrice = 0

totalOwned = 0

auto = True

while not over:
    if (auto):
        command = "auto"
    else:
        command = input("Enter command: ")

    price = d.price(ticker)
    
    if (command == "quit"):
        over = True
    
    if (command == "auto"):
        data = d.dataPoints(ticker, 0, 1)
        a.showIndicators(data)
        print("Price: $" + str(price))
        print("Total Owned: $" + str(totalOwned))
        reccomendation = a.strat(verbose = False)
        if (reccomendation == 1):
            command = "BUY"
        else:
            command = "SELL"
        
        if (owned):
            profit = (a.percentDiff(price, averagePrice) / 100) * amountInUSD
            print("Profit: $" + str(profit))
            if (profit > .5):
                command = "SELL"
                print("Taking profits")
    
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
        if (unitsOwned > 0):
            r.order_sell_crypto_by_price(ticker, amountInUSD*unitsOwned)
            print("Sold at $" + str(price))
            if (owned):
                profit = (a.percentDiff(price, averagePrice) / 100) * amountInUSD
                print("Profit: $" + str(profit))
            owned = False
            averagePrice = 0
            unitsOwned = 0
            totalOwned = 0
         
    if (auto):
        sleep(300)
    
    print('\n')
    
