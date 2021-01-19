import dataScrape as data
import analysis as a
from time import sleep

def train(step, dp, oldPrice, steps, macds, minutes=15):
    global failed
    if (step > 0):
        if (step == steps):
            print("Not enough data collected for training")
            a.append_list_as_row('prices.csv', [], 'a')
        
        price = 0
        try:
            price = data.price()
        except:
            print("Price scraping failed")
            failed = True

        if (step < (steps-1) and not failed):
            print('\n')
            print("Step: " + str(step))
            diff = price - oldPrice
            appreciation = diff / oldPrice
            appreciation *= 100
            appreciation = round(appreciation, 4)
            print("Total return: " + str(appreciation) + "%")

            print(dp)

            print("Current RSI: " + str(dp[0]))
            print("Current MACD: " + str(dp[1]))
            print("Current MA: " + str(dp[2]))
            print("Current EMA: " + str(dp[3]))
            macd = dp[1]
            print(macds)

            dp[1] = round(macds[1] - macds[0], 5)
            
            print(dp)

            if (appreciation > 0):
                appreciation = 1
            else:
                appreciation = 0

            a.store_csv_indicators(dp, minutes, 'prices.csv', appreciation)

            macds.pop(0)

            print("Updated dataset")

        
        try:
            dp = data.dataPoints()
            failed = False
        except:
            print("Datapoint scraping failed")
            print(data.dataPoints())
            failed = True
            sleep(120)
            train(step, [], 0, step, [], minutes)
        
        if (failed == False):
            oldPrice = price
            macds.append(dp[1])

        if (len(macds) == 3):
            macds.pop(0)
        
        sleep(60*minutes)
        train(step-1, dp, oldPrice, steps, macds, minutes)
    return steps


steps = int(input('Steps? '))

minutes = int(input("Time interval? "))

steps += 2

failed = False

train(steps, [], 0, steps, [], minutes)

print("Complete")