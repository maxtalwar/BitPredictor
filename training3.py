import dataScrape as d
import analysis as a
from time import sleep
import sys

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

for i in range (cycles):
    # spaces out the board and shows the current cycle
    print('\n')

    print(str(i+1) + ":" + str(cycles))

    # gets the data
    try:
        data = d.dataPoints(ticker, 0, api)
    except:
        print("Datapoint scraping failed")
        i -= 1
        sleep(300)
        continue

    # shows the data
    a.showIndicators(data)

    # waits until the data is old enough to measure its performance
    sleep(600)

    # gets the price
    price = d.price(ticker)

    # checks the price against the old price
    if (price > data[-1]):
        data[-1] = 1
    else:
        data[-1] = 0

    # shows how the asset performed based on the change
    print("CHANGE: " + str(data[-1]))

    # stores the data
    a.store_csv_indicators(data, 'prices.csv')