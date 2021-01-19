import analysis as a
import dataScrape as d
import robin_stocks as r
from regression import predict
from csv import *
from time import sleep
from datetime import datetime


def test(limit, time, startingHoldings):
    global total, correct, p, oldPrice, i, holdings, actions

    print(str(i+1) + ":" + str(limit))
    # prints current time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    try:
        price = d.price()
    except:
        print("getting price data failed")
        i += 1
        sleep(120)
        test(limit, time, startingHoldings)

    if (i > 0):
        print("Old Price: " + str(oldPrice))
        print("New Price: " + str(price))
        print("Previous Action: " + str(p))

        if (p != "HOLD"):
            if ((price > oldPrice) == p):
                correct += 1
                print("Correct")
            else:
                print("Incorrect")
            total += 1

        if (p == True):
            diff = price - oldPrice
            diff /= oldPrice
            holdings *= (diff + 1)
            diff *= 100
            print("Appreciation " + str(diff) + "%")

    if (i < limit-1):

        headers = ["RSI","MA","EMA", "TIME","CHANGE"]

        indicators = d.dataPoints()

        indicators.append(float(time))

        #indicators.append("")

        a.showIndicators(indicators)

        print("HOLDINGS: $" + str(holdings))

        a.append_list_as_row("predict.csv", headers, 'w')

        a.append_list_as_row("predict.csv", indicators, 'a')

        p = a.strat(indicators)

        if (p == True):
            print("Bought")
            actions.append(p)
        if (p == False):
            print("Sold")
            actions.append(p)
        if (p == "HOLD"):
            print("Held")
            actions.append(p)

            if (indicators[2] < indicators[1]):
                print("The EMA was less than the MA, which fulfills the condition for buying. However the RSI is equal to " + str(indicators[0]) + ", which does not fit the criteria specified ")
            else:
                print("The EMA was greater than the MA, which fulfills the condition for selling. However, the RSI is equal to " + str(indicators[0]) + ", which does not fit the criteria for selling ")
        
        oldPrice = price
        print('\n')
        
        if (p != "HOLD"):
            sleep(600)
        else:
            sleep(time*60)
        i += 1

        sleep(15)
        test(limit, time, startingHoldings)
    
    return ((correct/total)*100)


total = 0

correct = 0

p = False

actions = []

oldPrice = 0

i = 0

limit = int(input("Limit: "))

startingHoldings = int(input("Starting holdings: "))

time = float(input("Time? "))

holdings = startingHoldings

originalPrice = d.price()

print('\n')

print("Warming up...")

sleep(15)

print("Starting...")

print('\n')

accuracy = test(limit, time, startingHoldings)

print("Correct trades: " + str(correct))
print("Total trades: " + str(total))

if (total == 0):
    print("No trades made, so accuracy cannot be assessed")
else:
    print("Correct percentage: " + str(accuracy) + "%")


price = d.price()

diff = a.percentDiff(price, originalPrice)

percent = price / originalPrice

percent = percent * startingHoldings

print("\n")

print("Asset appreciation: " + str(diff) + "%")

print(str(startingHoldings) +  " HODLING would have turned into: $" + str(percent))

print(str(startingHoldings) + " with the alg would have turned into: $" + str(holdings))

print("You profited $" + str(holdings - startingHoldings) + " over the course of " + str(limit*time) + " minutes")

print(actions)