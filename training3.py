import dataScrape as d
import analysis as a
from time import sleep
import sys
import robin_stocks as r

d.login()

# Definte the arguments
args = sys.argv
argsDict = {}

ticker = 'BTC'

if ('-api' in args):
    argsDict['api'] = int(args[args.index('-api') + 1])
else:
    argsDict['api'] = 1

if ('-cycles' in args):
    argsDict['cycles'] = int(args[args.index('-cycles') + 1])
else:
    argsDict['cycles'] = int(input("Cycles: "))

if ('-delay' in args):
    argsDict['delay'] = int(args[args.index('-delay') + 1])
else:
    argsDict['delay'] = 0

if ('-ticker' in args):
    argsDict['ticker'] = str(args[args.index('-ticker') + 1])
else:
    ticker = 'BTC'

api = argsDict['api']
cycles = argsDict['cycles']
delay = argsDict['delay']

sleep(delay)

a.append_list_as_row('prices.csv', [], 'a')

for i in range (cycles):
    # spaces out the board and shows the current cycle
    print('\n')
    print(str(i+1) + ":" + str(cycles))

    # gets the data
    data = d.dataPoints(ticker, api)

    # shows the data
    a.showIndicators(data)

    # sets the old price
    try:
        oldPrice = d.price(ticker)
    except:
        # Logs into Robinhood
        login = d.login()
        oldPrice = d.price(ticker)
    
    # adds the price to the dataset
    data.append(oldPrice)

    # waits until the data is old enough to measure its performance
    sleep(600)

    # gets the price
    try:
        price = d.price(ticker)
    except:
        # Logs into Robinhood
        login = d.login()
        price = d.price(ticker)

    # displays the old price and the price
    print("Old Price: " + str(oldPrice))
    print("Price: " + str(price))

    # checks the price against the old price
    if (price > oldPrice):
        data[-1] = 1
    else:
        data[-1] = 0

    # shows how the asset performed based on the change
    print("CHANGE: " + str(data[-1]))

    # filters and then stores the data
    if (data[0] > 65 and data[-1] == 1):
        print("Filtered out outlier (high RSI and gain)")
    elif (data[0] < 30 and data[-1] == 0):
        print("Filtered out outlier (low RSI and negative change)")
    else:
        a.store_csv_indicators(data, 'prices.csv')