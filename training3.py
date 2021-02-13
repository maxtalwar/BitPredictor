import dataScrape as d
import analysis as a
from time import sleep
import sys
import robin_stocks as r

# Definte the arguments
args = sys.argv
argsDict = {}

ticker = 'BTC'

if ('-api' in args):
    argsDict['api'] = int(args[args.index('-api') + 1])
else:
    argsDict['api'] = int(input("API #: "))

if ('-cycles' in args):
    argsDict['cycles'] = int(args[args.index('-cycles') + 1])
else:
    argsDict['cycles'] = int(input("Cycles: "))

if ('-delay' in args):
    argsDict['delay'] = int(args[args.index('-delay') + 1])
else:
    argsDict['delay'] = 0

if ('-ticker' in args):
    argsDict['ticker'] = int(args[args.index('-ticker') + 1])
else:
    ticker = 'BTC'

api = argsDict['api']

cycles = argsDict['cycles']

delay = argsDict['delay']

sleep(delay)

a.append_list_as_row('prices.csv', [], 'a')

print("IMPORTANT: IF YOU HAVE NOT ALREADY IMPLEMENTED THIS, THERE IS A MUCH MORE ACCURATE WAY TO MODEL THE PREDICTIONS. ")
print("THE WAY TO DO THIS IS: create dozens of predictions and store them in a dictionary, with the accuracy of that prediction model as the key and the prediction value as the key's corresponding value. ")
print("Check the highest accuracy value in the dictionary, and plug that in. You should then take action based on what that corresponding key value is. ")
print("For example: say you generate 10 predictions. 7 of those predictions say to sell, 3 say to buy. You would think that you are supposed to buy right now. However, that is not the case. Look through the accuracy of every prediction model that you have created")
print("For the sake of example, lets say the most accurate model was 80 percent accurate and that model (with 80 percent accuracy) predicted that you should buy")
print("That is the prediction you will want to go for. You can try averaging out all the accuracy values for buy and sell (so average the accuracy of all the models that say buy and the accuracy of all the models that say sell")
print("I think you get the picture here. This model is very similar to the concept of a random forest. It's a random forest of boosted trees. This will probably take a long time to model and train, so make sure to close out everything you don't need and opimize the program for performance. Also, invest in a better GPU if possible. ")

for i in range (cycles):
    # spaces out the board and shows the current cycle
    print('\n')

    print(str(i+1) + ":" + str(cycles))

    # gets the data
    try:
        data = d.dataPoints(ticker, 0, api)
    except:
        print("Datapoint scraping failed - redirecting api")
        if (api == 1):
            api = 0
        else:
            api = 1
        data = d.dataPoints(ticker, 0, api)

    # shows the data
    a.showIndicators(data)

    # waits until the data is old enough to measure its performance
    sleep(600)

    # gets the price
    try:
        price = d.price(ticker)
    except:
        # Logs into Robinhood
        login = r.login(username="maxnmtalwar@gmail.com", password="8#k5uqP9NG@n", expiresIn=86400, by_sms=True)
        price = d.price(ticker)

    # displays the old price and the price
    print("Old Price: " + str(data[-1]))
    print("Price: " + str(price))

    # checks the price against the old price
    if (price > data[-1]):
        data[-1] = 1
    else:
        data[-1] = 0

    # shows how the asset performed based on the change
    print("CHANGE: " + str(data[-1]))

    # stores the data
    a.store_csv_indicators(data, 'prices.csv')