import dataScrape as data
from time import sleep
import analysis as a

ticker = "BTC"

headers = a.getHeaders()
api = 1
amountInUSD = 100
totalProfit = 0
total = 0
correct = 0
owned = False

for i in range(12):

    print("Cycle: " + str(i+1))

    # gets the data
    indicators = data.dataPoints(ticker, api)
    oldPrice = data.price(ticker)

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
        print("BOUGHT")
    if (prediction == 0):
        print("SOLD")

    sleep(900)

    price = data.price(ticker)

    print("Old Price: $" + str(oldPrice))
    print("Price: $" + str(price))
    
    if (prediction == 1):
        if (price > oldPrice):
            correct += 1
            print("Correct")
        else:
            print("Incorrect")
    elif (prediction == 0):
        if (price < oldPrice):
            correct += 1
            print("Correct")
        else:
            print("Incorrect")
    total += 1

    if (owned):
        profit = (a.percentDiff(price, oldPrice)/100) * amountInUSD
        totalProfit += profit
        print("Profit: $" + str(profit))
    
    owned = False
    
    print('\n')

print(correct)
print(total)

percentage = (correct / total) * 100

print("Correct percentage: " + str(percentage))
print("Total Profit: $" + str(totalProfit))