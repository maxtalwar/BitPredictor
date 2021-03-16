import dataScrape as d
from time import sleep
import analysis as a
import robin_stocks as r

d.login()

ticker = "BTC"

api = 1

headers = a.getHeaders()

amountInUSD = 200

totalProfit = 0

owned = False

startingCash = r.account.load_phoenix_account(info=None)['account_buying_power']['amount']

print("Cash: $" + str(startingCash))

for i in range(12):

    print("Cycle: " + str(i+1))
    # gets and prepares the data
    indicators = d.dataPoints(ticker, api)
    price = d.price(ticker)
    indicators.append("")
    
    # adds the predict data to a csv file
    a.append_list_as_row('predict.csv', headers, 'w')
    a.append_list_as_row("predict.csv", indicators, 'a')
    a.showIndicators(indicators)

    # generate a prediction
    prediction = a.strat()

    amountInAsset = round(amountInUSD/price, 4)

    # checks if the bot should buy
    if (prediction == 1):
        owned = True
        r.order_buy_crypto_by_quantity(ticker, amountInAsset)
        print("BOUGHT")
    if (prediction == 0):
        print("Reccomended action: SELL")

    oldPrice = price
    price = d.price(ticker)

    print("Old Price: $" + str(oldPrice))
    print("Price: $" + str(price))

    # repeatedly scans until the trade has become profitable - when it has, sell
    if (owned):
        for i in range(10):
            sleep(30)
            price = d.price(ticker)
            profit = (a.percentDiff(price, oldPrice)/100) * amountInUSD
            print("Price: $" + str(price))
            print("Profit: $" + str(profit))
            if (profit > .2):
                totalProfit += profit
                r.order_sell_crypto_by_quantity(ticker, amountInAsset)
                print("SOLD")
                break
    else:
        sleep(65)
    
    owned = False
    
    print('\n')

print("Total Profit: $" + str(totalProfit))

sleep(120)

finalCash = r.account.load_phoenix_account(info=None)['account_buying_power']['amount']

print("Final Cash: $" + str(finalCash))