import analysis as a
import dataScrape as d
import robin_stocks as r
from regression import predict
from csv import *
from time import sleep
from datetime import datetime
import emailClient as email

def test(limit, time, startingHoldings):
    global total, correct, p, oldPrice, i, holdings, actions

    if (i < limit+1):
        print(str(i) + ":" + str(limit))
    
    # prints current time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    try:
        price = d.price('BTC')
    except:
        d.login()
        price = d.price('BTC')

    if (i > 1):
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

    if (i < limit+1):

        headers = a.setHeaders()

        try:
            indicators = d.dataPoints('BTC', API = 0)
        except:
            indicators = d.dataPoints('BTC', API = 1)
        
        indicators.pop()

        indicators.append("")

        a.showIndicators(indicators)

        print("HOLDINGS: $" + str(holdings))

        a.append_list_as_row("predict.csv", headers, 'w')

        a.append_list_as_row("predict.csv", indicators, 'a')

        p = a.strat(indicators, verbose = False)

        if (p == True):
            print("Bought")
            actions.append(p)
        if (p == False):
            print("Sold")
            actions.append(p)
        
        oldPrice = price
        print('\n')
        
        if (p != "HOLD"):
            sleep(time*60)
        else:
            sleep(120)
        i += 1

        sleep(15)
        test(limit, time, startingHoldings)
    
    return ((correct/total)*100)

ticker = "BTC"

total = 0

correct = 0

p = False

actions = []

oldPrice = 0

i = 1

limit = int(input("Limit: "))

startingHoldings = int(input("Starting holdings: "))

time = float(input("Time? "))

holdings = startingHoldings

originalPrice = d.price(ticker)

print('\n')

print("Warming up...")

sleep(15)

print("Starting...")

print('\n')

sleep(60)

accuracy = test(limit, time, startingHoldings)

print("Correct trades: " + str(correct))
print("Total trades: " + str(total))

if (total == 0):
    print("No trades made, so accuracy cannot be assessed")
else:
    print("Correct percentage: " + str(accuracy) + "%")


price = d.price(ticker)

diff = a.percentDiff(price, originalPrice)

percent = price / originalPrice

percent = percent * startingHoldings

print("\n")

print("Asset appreciation: " + str(diff) + "%")

print("$" + str(startingHoldings) +  " HODLING would have turned into: $" + str(percent))

print("$" + str(startingHoldings) + " with the alg would have turned into: $" + str(holdings))

print("You profited $" + str(holdings - startingHoldings) + " over the course of " + str(limit*time) + " minutes")