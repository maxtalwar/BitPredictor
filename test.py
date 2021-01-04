import analysis as a
import dataScrape as d
import robin_stocks as r
from regression import predict
from csv import *
from time import sleep

# Function for appending values to a CSV files (from a list)
def append_list_as_row(file_name, list_of_elem, action):
    # Open file in append mode
    with open(file_name, action, newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj, lineterminator='\n')
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
    write_obj.close()


total = 0

correct = 0

buy = False

change = False

oldPrice = 0

i = 0

limit = int(input("Limit: "))

startingHoldings = int(input("Starting holdings: "))

time = int(input("Time? "))

holdings = startingHoldings

originalPrice = d.price()

def test(limit, time, startingHoldings, oldMACD = 0):
    global total, correct, buy, oldPrice, i, holdings, change

    try:
        price = d.price()
    except:
        print("getting price data failed")
        i += 1
        macd = d.dataPoints()[1]
        test(limit, time, startingHoldings, macd)
        sleep(120)

    if (i > 0):
        print(oldPrice)
        print(price)
        print(buy)
        if ((price > oldPrice) == buy):
            correct += 1
            print("correct")
        else:
            print("Incorrect")
        total += 1

        if (buy):
            diff = price - oldPrice
            diff /= oldPrice
            holdings *= (diff + 1)
            diff *= 100
            print("Appreciation " + str(diff) + "%")

    if (i < limit):
        print(str(i+1) + ":" + str(limit))

        headers = ["RSI","MACD","MA","EMA", "TIME","CHANGE"]

        append_list_as_row("predict.csv", headers, 'w')

        dp = d.dataPoints()
        dp.append(float(time))

        macd = dp[1]

        dp[1] = round((macd - oldMACD), 6)

        dp.append("")
        print(dp)

        append_list_as_row("predict.csv", dp, 'a')

        p = a.stratAI()

        if (p):
            buy = True
            print("Bought")
        else:
            buy = False
            change = Trues
            print("Sold")
        
        print("HOLDINGS: $" + str(holdings))
        oldPrice = price
        print('\n')
        sleep(time*60)
        i += 1
        test(limit, time, startingHoldings, macd)
    
    return ((correct/total)*100)

test(limit, time, startingHoldings)


print("Correct trades: " + str(correct))
print("Total trades: " + str(total))
print("Correct percentage: " + str((correct/total)*100) + "%")


price = d.price()

diff = a.percentDiff(price, originalPrice)

percent = price / originalPrice

percent = percent * startingHoldings

print("\n")

print("Asset appreciation: " + str(diff) + "%")

print(str(startingHoldings) +  " HODLING would have turned into: $" + str(percent))

print(str(startingHoldings) + " with the alg would have turned into: $" + str(holdings))

print("You profited $" + str(holdings - startingHoldings) + " over the course of " + str(limit*time) + " minutes")

print(change)