import dataScrape as d
import analysis as a
from time import sleep

for i in range (200):

    sleep(300)

    print('\n')

    print(i+1)

    try:
        data = d.dataPointsTwo(ticker = 'BTC', backTrack = 10)
    except:
        print("Datapoint scraping failed")
        i -= 1
        sleep(40)
        continue

    if (data[-1] > data[-2]):
        data[-2] = 1
    else:
        data[-2] = 0
        
    data.pop()

    a.showIndicators(data)

    print("CHANGE: " + str(data[-1]))

    a.store_csv_indicators(data, 'prices.csv')