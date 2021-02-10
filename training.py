import dataScrape as data
import analysis as a
from time import sleep

def train(steps, dp, oldPrice, step, minutes, ticker):
    global failed
    if (step < steps+1):
        print(str(step) + ":" + str(steps))
        if (step == 0):
            print("Not enough data collected for training")
            a.append_list_as_row('prices.csv', [], 'a')

        try:
            price = data.price(ticker)
        except:
            print("Price scraping failed")
            failed = True

        if (not failed and step > 0):
            print("Indicators from previous cycle: ")
            a.showIndicators(dp)
            appreciation = round(a.percentDiff(price, oldPrice), 4)

            print("Old Price " + str(oldPrice))
            print("Current Price: " + str(price))
            print("Total return: " + str(appreciation) + "%")

            if (appreciation > .025 or appreciation < -.025):
                if (appreciation > 0):
                    appreciation = 1
                else:
                    appreciation = 0
                
                a.store_csv_indicators(dp, 'prices.csv', appreciation)
                print("Updated dataset")
            else:
                print("Filtered out noise (not significant enough change)")
        if (step < steps + 1):
            dp = data.dataPoints(ticker)
            
            oldPrice = price

            print('\n')
            sleep(60*minutes)
            train(steps, dp, oldPrice, step+1, minutes, ticker)
    return steps

steps = int(input('Steps? '))

minutes = int(input("Time interval? "))

ticker = 'BTC'

failed = False

sleep(120)

train(steps, [], 0, 0, minutes, ticker)