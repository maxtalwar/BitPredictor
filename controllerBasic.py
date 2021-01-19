import dataScrape as data
import analysis as a
from time import sleep
import robin_stocks as r
from datetime import datetime

owned = False

sleep(15)

amountInAsset = round(30/data.price(), 5)

for i in range (10):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    headers = ["RSI","MA","EMA", "TIME","CHANGE"]

    indicators = data.dataPoints()

    indicators.append(10)

    a.append_list_as_row('predict.csv', headers, 'w')

    a.append_list_as_row("predict.csv", indicators, 'a')

    a.showIndicators(indicators)

    predict = a.strat(indicators)

    price = data.price()

    if (owned and predict == "HOLD"):
        if (((price - purchasePrice) / purchasePrice)*100 >= .75):
            owned = False
            data.sell('BCH', amountInAsset)
            print("Sold Asset (Taking gains)")

    elif (predict == True and not owned):
        purchasePrice = price
        owned = True
        data.buy("BCH", amountInAsset)
    
    elif (predict == False and owned):
        owned = False
        data.sell('BCH', amountInAsset)
    
    elif (predict == "HOLD"):
        print("Held")
    else:
        if (owned):
            print("No action taken: already owned")
        else:
            print("No action taken: not owned")
    
    print('\n')

    sleep(120)

if (owned):
    r.order_sell_crypto_by_quantity('BCH', amountInAsset)
    print("Sold all assets - closed out")


print("Complete")