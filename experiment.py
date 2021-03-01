import robin_stocks as r
import dataScrape as d
import regression
import analysis as a
from time import sleep
import csv
import pandas as pd
import emailClient as email
import statistics as stats

d.login()

"""amount = int(input("Much much to trade on? "))

print(data.price())

amountInAsset = round(float(amount / data.price()), 7)

print(amountInAsset)


r.order_buy_crypto_by_quantity("BCH", amountInAsset)"""


"""headers = ["RSI","MACD","MA","EMA", "STOCH_RSI", "TIME","CHANGE"]

append_list_as_row("predict.csv", headers, 'w')

dp = d.dataPoints()
dp.append(float(5))
dp.append("")

append_list_as_row("predict.csv", dp, 'a')"""




"""for i in range(10):
    print(i)
    try:
        print(d.price())
    except:
        print("Current cycle failed")
    sleep(120)"""


"""message = email.createMessage("BitTrader", 3)
email.sendEmail(message)"""

#sleep(60)

"""dp = d.dataPoints(ticker = 'DOGE')
a.showIndicators(dp)"""

"""ticker = 'BTC'

dp = d.dataPoints(ticker)

print(dp)"""

#print(regression.predict())

"""print("IMPORTANT: IF YOU HAVE NOT ALREADY IMPLEMENTED THIS, THERE IS A MUCH MORE ACCURATE WAY TO MODEL THE PREDICTIONS. ")
print("THE WAY TO DO THIS IS: create dozens of predictions and store them in a dictionary, with the accuracy of that prediction model as the key and the prediction value as the key's corresponding value. ")
print("Check the highest accuracy value in the dictionary, and plug that in to the dictionary. You should then take action based on what that corresponding key value is. ")
print("For example: say you generate 10 predictions. 7 of those predictions say to sell, 3 say to buy. You would think that you are supposed to buy right now. However, that might not be the case. Look through the accuracy of every prediction model that you have created")
print("For the sake of example, lets say the most accurate model was 80 percent accurate and that model (with 80 percent accuracy) predicted that you should buy")
print("That is the prediction you will want to go for. You can try averaging out all the accuracy values for buy and sell (so average the accuracy of all the models that say buy and the accuracy of all the models that say sell")
print("I think you get the picture here. This model is very similar to the concept of a random forest. It's a random forest of boosted trees. This will probably take a long time to model and train, so make sure to close out everything you don't need and opimize the program for performance. Also, invest in a better GPU if possible. You currently have a 1660 ti, which is efficient but fairly slow. ")"""

"""
predictions = []

accuracy = []

best = 0

for i in range(100):
    results = regression.predict()
    accuracy.append(results[1])
    predictions.append(results)
    #print(str(results[1]) + ":" + str(results[0]))
    if (results[1] > best):
        best = results[1]
        prediction = results[0]

print(prediction)
print(best)

averageAccuracy = a.average(accuracy)*100

minAccuracy = min(accuracy)*100

medianAccuracy = stats.median(accuracy)*100

print("Mean Accuracy: " + str(averageAccuracy) + "%")

print("Lowest Accuracy: " + str(minAccuracy) + "%")

print("Median Accuracy: " + str(medianAccuracy) + "%")

print('\n')"""

"""

print("Good signs: ")

if (averageAccuracy > 50):
    print("The average accuracy was more than 50%")

if (minAccuracy > 50):
    print("The minimum accuracy was more than 50%")

if (medianAccuracy > 50):
    print("The median accuracy was more than 50%")

print('\n')

print("Bad signs: ")

if (minAccuracy < 50):
    print("The lowest accuracy was less than 50%, which is an indicator that the bot may lose money in some cases")
"""

"""
correct = 0

total = 0

# generates predictions and compares them to the target value - generates a percentage score based on the predictions
for i in range(20):
    prediction = a.stratAITwo()
    print(prediction)
    if (prediction == 0):
        correct += 1
    total += 1
    print('\n')

print(correct)
print(total)

print(100*correct / total)"""

"""d.login()

ticker = 'BTC'

price = d.price(ticker)
print(price)

amountInAsset = round(30/price, 4)

d.buy(ticker, amountInAsset)"""

ticker = "BTC"

amountInAsset = round(100 / d.price(ticker), 5)

r.order_sell_crypto_by_quantity(ticker, amountInAsset*1)