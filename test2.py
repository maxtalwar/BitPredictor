import dataScrape as d
from time import sleep
import analysis as a

startingCash = float(input("Starting cash: "))

ticker = "BTC"

api = 1

headers = a.getHeaders()

amountInUSD = 100

totalProfit = 0

total = 0

correct = 0

owned = False

for i in range(10):
    # gets the data
    indicators = d.dataPoints(ticker, api)
    oldPrice = d.price(ticker)

    # adds a comma value to the data so it works with a csv file
    indicators.append("")

    # adds the predict data to a csv file
    a.append_list_as_row('predict.csv', headers, 'w')
    a.append_list_as_row("predict.csv", indicators, 'a')
    a.showIndicators(indicators)

    prediction = a.strat()

    amountInAsset = round(amountInUSD/oldPrice, 5)

    if (prediction == 1):
        owned = True
    if (prediction == 0):
        owned = False

    sleep(600)

    price = d.price(ticker)

    if (price > oldPrice):
        correct += 1
    total += 1

    print("Old Price: $" + str(oldPrice))
    print("Price: $" + str(price))

    if (owned):
        profit = amountInAsset*price - amountInUSD
        totalProfit += profit
        print("Profit: $" + str(profit))
    
    print('\n')

percentage = (correct / total) * 100

print("Correct percentage: " + str(percentage))


