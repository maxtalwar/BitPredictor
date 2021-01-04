from regression import predict
import dataScrape as data
import analysis as a
import robin_stocks as r
from time import sleep
from datetime import datetime
import pync

steps = int(input("How many cycles? "))

if (steps > 25):
    halfway = round(steps/2)
else:
    halfway = 0

time = int(input("How many minutes between each cycle? "))

amount = int(input("Much much to trade on? "))

amountInAsset = round(float(amount / data.price()), 7)

#print(amountInAsset)

holdings = amount

startingHoldings = holdings

# Logs into Robinhood
login = r.login(username="maxnmtalwar@gmail.com",
         password="8#k5uqP9NG@n",
         expiresIn=86400,
         by_sms=True)

print("Logged in")

owned = False

buy = False

correct = 0

total = 0

originalPrice = data.price()

diff = 0

suspended = False

print('\n')

def cycle(step, oldPrice, purchasePrice, appreciation, steps, time, amount, oldIndicators):
    global owned, correct, total, holdings, diff, halfway, suspended

    
    if (step > 0):
        if (step == halfway):
            suspension = True
            print("Suspended")
        
        headers = ["RSI","MACD","MA","EMA", "TIME","CHANGE"]

        a.append_list_as_row('predict.csv', headers, 'w')

        indicators = data.dataPoints()

        macd = indicators[1]

        if (oldIndicators[1] < macd):
            results = 1
        else:
            results = 0

        placeholder = [indicators[0], results, indicators[2], indicators[3], indicators[4]]

        a.store_csv_indicators(placeholder, time, 'predict.csv')

        print("Predict data set up")

        print("Current RSI: " + str(indicators[0]))
        print("Current MACD: " + str(indicators[1]))
        print("Current MA: " + str(indicators[2]))
        print("Current EMA: " + str(indicators[3]))

        price = data.price()
        print("Current price of BCH: $" + str(price))

        if (owned):
            """diff = price - purchasePrice
            appreciation = diff / purchasePrice
            appreciation *= 100
            print("Total return: " + str(appreciation) + "%")"""
            diff = price - oldPrice
            diff /= oldPrice
            holdings *= (diff + 1)
            diff *= 100
            print("Asset Appreciation " + str(diff) + "%")

            diff = a.percentDiff(price, purchasePrice)
            print("Return on previous purchase: " + str(diff) + "%")
            print("HOLDINGS: " + str(holdings))
        
        prediction = a.stratAI()

        print("Predicted asset appreciation: " + str(prediction))
        
        if (diff > 1):
            #r.order_sell_crypto_by_price('BCH', amount, timeInForce='gtc')
            print("Sold asset (Taking gains)")
            pync.notify('Sold asset (Taking gains)', title='BitTrader')
            owned = False
        elif (prediction == True and not owned and not suspended):
            #r.order_buy_crypto_by_quantity("BCH", amountInAsset)
            print("Bought asset")
            pync.notify('Bought Asset', title='BitTrader')
            owned = True
            purchasePrice = price
        elif (prediction == False and owned and not suspended):
            #r.order_sell_crypto_by_quantity('BCH', amountInAsset)
            print("Sold asset")
            pync.notify('Sold Asset', title='BitTrader')
            owned = False
        else:
            if (not owned):
                print("No action taken: not owned")
            if (owned):
                print("No action taken: already owned")
            if (suspended):
                print("No action taken: program suspended")

            #pync.notify('No action taken', title='BitTrader')

        # prints current time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        
        sleep(time*60)
        print('\n')
        cycle(step-1, price, purchasePrice, appreciation, steps, time, amount, indicators)

cycle(steps, 0, 0, 0, steps, time, amount, [0, 0, 0, 0, 0])

if owned:
    r.order_sell_crypto_by_quantity('BCH', amountInAsset, timeInForce='gtc')
    print("Closing out - sold assets")

pync.notify('Program complete', title='BitTrader')

# Notes:
# if the EMA is more than the MA and the MA has begun to trend upwards, it 
# means the asset just exited a short bull run and will begin to go up

price = data.price()

diff = a.percentDiff(price, originalPrice)


percent = price / originalPrice

percent = percent * startingHoldings

print("Original Price $" + str(originalPrice))

print("Current Price $" + str(price))

print("\n")

print("Asset appreciation: " + str(diff) + "%")

print("$" + str(startingHoldings) +  " HODLING turned into: $" + str(percent))


print("$" + str(startingHoldings) + " with the alg turned into: $" + str(holdings))

print("You profited $" + str(holdings - startingHoldings) + " over the course of " + str(steps*time) + " minutes")