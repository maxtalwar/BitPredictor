import dataScrape as d
import analysis as a
import robin_stocks as r
from time import sleep

d.login()

ticker = str(input("Ticker: "))

over = False

owned = False

amountInUSD = 100

amountInAsset = round(amountInUSD / d.price(ticker), 5)

unitsOwned = 0

averagePrice = 0

totalOwned = 0

auto = False

cycles = 0

print('\n')

def checkProfit(totalOwned, price, unitsOwned, amountInUSD):
    return ((totalOwned*price - unitsOwned*amountInUSD) >= 1)

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
        print("Total Owned: $" + str(totalOwned*price))
        reccomendation = a.strat(verbose = False)
        if (reccomendation == 1):
            command = "BUY"
        else:
            command = "SELL"
        print("Predicted action: " + str(command))
        
        if (owned):
            profit = totalOwned*price - unitsOwned*amountInUSD
            print("Current Profit: $" + str(profit))
            if (profit > 1):
                command = "SELL"
                print("Taking profits")
    
    if (command == "price"):
        print("Price: $" + str(price))
        print("Total Owned: $" + str(totalOwned*price))
        if (owned):
            profit = (totalOwned*price - unitsOwned*amountInUSD)
            print("Profit: $" + str(profit))
    
    if (command == "show"):
        data = d.dataPoints(ticker, 0, 1)
        reccomendation = a.strat(verbose = False)
        a.showIndicators(data)
        if reccomendation == 1:
            print("Reccomended action: BUY")
        else:
            print("Reccomended action: SELL")
    
    if (command == "TRAILINGBUY"):
        price = d.price(ticker)
        amountInAsset = round(amountInUSD / price, 5)
        r.order_buy_crypto_by_quantity(ticker, amountInAsset)
        print("Bought at $" + str(price))
        owned = True
        totalOwned += amountInAsset
        unitsOwned += 1
        averagePrice = totalOwned * price / unitsOwned

        profit = (totalOwned*price - unitsOwned*amountInUSD)
        while (profit < .75):
            sleep(10)
            price = d.price(ticker)
            profit = (totalOwned*price - unitsOwned*amountInUSD)
            print("Profit: $" + str(profit))
        
        command = "SELL"

    if (command == "BUY"):
        price = d.price(ticker)
        if (unitsOwned <= 2):
            amountInAsset = round(amountInUSD / price, 5)
            r.order_buy_crypto_by_quantity(ticker, amountInAsset)
            print("Bought at $" + str(price))
            owned = True
            totalOwned += amountInAsset
            unitsOwned += 1
            averagePrice = totalOwned * price / unitsOwned

    if (command == "SELL"):
        price = d.price(ticker)
        if (unitsOwned > 0):
            print("Asset owned: " + str(totalOwned))
            r.order_sell_crypto_by_quantity(ticker, totalOwned)
            print("Sold at $" + str(price))
            if (owned):
                profit = (totalOwned*price - unitsOwned*amountInUSD)
                print("Sale Profit: $" + str(profit))
            owned = False
            averagePrice = 0
            unitsOwned = 0
            totalOwned = 0
    
    print('\n')
    
    if (auto):
        cycles += 1
        if (cycles == 100):
            over = True
        else:
            for i in range(10):
                price = d.price(ticker)
                if (not checkProfit(totalOwned, price, unitsOwned, amountInUSD)):
                    sleep(30)

if (owned):
    r.order_sell_crypto_by_price(ticker, amountInUSD*unitsOwned)