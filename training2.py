import dataScrape as data
import analysis as a
from time import sleep
import requests, json
import robin_stocks as r
import analysis as a
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def train(limit, i, oldPrice):
    if (i < limit+1):
        price = data.price()
        if (i > 0):
            if (price > oldPrice):
                appreciation = 1
            else:
                appreciation = 0
        
            dp = data.dataPoints(1)

            print("Indicators from previous cycle: ")
            a.showIndicators(dp)
            diff = price - oldPrice
            appreciation = diff / oldPrice
            appreciation *= 100
            appreciation = round(appreciation, 4)
            print("Old Price " + str(oldPrice))
            print("Current Price: " + str(price))
            print("Total return: " + str(appreciation) + "%")
                    

train(int(input("Limit: ")), 0, 0)