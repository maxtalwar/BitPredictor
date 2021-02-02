import robin_stocks as r
import dataScrape as d
import regression
import analysis as a
from time import sleep
import csv
import pandas as pd
import emailClient as email

# Logs into Robinhood
login = r.login(username="maxnmtalwar@gmail.com",
         password="8#k5uqP9NG@n",
         expiresIn=86400,
         by_sms=True)

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

print(regression.predict())