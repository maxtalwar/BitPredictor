import dataScrape as data
import analysis as a
from time import sleep
import robin_stocks as r
from datetime import datetime

owned = False

sleep(15)

ticker = "BTC"

amountInAsset = round(30/data.price(ticker), 5)

api = 0

for i in range (10):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print("Current Time =", current_time)

  headers = a.setHeaders()

  try:
    indicators = data.dataPoints(ticker, 0, api)
  except:
    print("Datapoint scraping failed - redirecting api")
    if (api == 1):
        api = 0
    else:
        api = 1
    indicators = data.dataPoints(ticker, 0, api)

  a.append_list_as_row('predict.csv', headers, 'w')

  a.append_list_as_row("predict.csv", indicators, 'a')

  a.showIndicators(indicators)

  predict = a.strat(indicators, verbose = False)

  price = data.price()
  
  if (predict and not owned):
    purchasePrice = price
    owned = True
    data.buy(ticker, amountInAsset)
  
  elif (predict and owned):
    if (((price - purchasePrice) / purchasePrice)*100 >= .75):
        owned = False
        data.sell(ticker, amountInAsset)
        print("Sold Asset (Taking gains)")
  
  elif (not predict and owned):
    owned = False
    data.sell(ticker, amountInAsset)
  
  elif (predict == "HOLD"):
    owned = False
    data.sell(ticker, amountInAsset)
  else:
    if (owned):
        print("No action taken: already owned")
    else:
        print("No action taken: not owned")
  
  print('\n')

  sleep(600)

if (owned):
    r.order_sell_crypto_by_quantity(ticker, amountInAsset)
    print("Sold all assets - closed out")


print("Complete")