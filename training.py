import dataScrape as data
import analysis as a
from time import sleep

def train(steps, dp, oldPrice, step, minutes):
    global failed
    if (step < steps):
        print(str(step) + ":" + str(steps))
        if (step == 0):
            print("Not enough data collected for training")
            a.append_list_as_row('prices.csv', [], 'a')

        try:
            price = data.price()
        except:
            print("Price scraping failed")
            failed = True

        if (not failed and step > 0):
            print("Indicators from previous cycle: ")
            a.showIndicators(dp)
            diff = price - oldPrice
            appreciation = diff / oldPrice
            appreciation *= 100
            appreciation = round(appreciation, 4)
            print("Old Price " + str(oldPrice))
            print("Current Price: " + str(price))
            print("Total return: " + str(appreciation) + "%")

            if (appreciation > .09 or appreciation < -.09):
                if (appreciation > 0):
                    appreciation = 1
                else:
                    appreciation = 0
                
                a.store_csv_indicators(dp, minutes, 'prices.csv', appreciation)
                print("Updated dataset")
            else:
                print("Filtered out noise (not significant enough change)")
        
        try:
            dp = data.dataPoints()
            failed = False
        except:
            print("Datapoint scraping failed")
            failed = True
        
        if (not failed):
            oldPrice = price

        print('\n')
        sleep(60*minutes)
        train(steps, dp, oldPrice, step+1, minutes)
    return steps

steps = int(input('Steps? '))

minutes = int(input("Time interval? "))

sleep(20)

failed = False

train(steps, [], 0, 0, minutes)

print("Complete")