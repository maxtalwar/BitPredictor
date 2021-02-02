import dataScrape as data
from time import sleep


sleep(30)
owned = False
# For loop, cycles through scans
for i in range(100):
# checks RSI value
    print("RSI: " + str(data.RSI('BTC')))
    if (data.RSI('BTC') < 35 and not owned):
        data.buy("BTC", .0005)
        owned = True
        print("Bought: $" + str(data.price()))
    elif (data.RSI('BTC') > 65 and owned):
        data.sell("BTC", .0005)
        owned = False
        print("Sold: $" + str(data.price()))
    else:
        print("No action taken")
    
    sleep(90)
# checks if owned or not

# waits, repeats