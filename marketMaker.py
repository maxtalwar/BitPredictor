import dataScrape as data  
from time import sleep
import robin_stocks as r

# Logs into Robinhood
login = r.login(username="maxnmtalwar@gmail.com",
         password="8#k5uqP9NG@n",
         expiresIn=86400,
         by_sms=True)


for i in range (10):
    ask_price = data.price('ask_price')

    bid_price = data.price('bid_price')

    print("Ask Price: " + str(ask_price))

    print("Bid Price: " + str(bid_price))

    if (ask_price > bid_price):
        r.order_buy_crypto_by_quantity("BCH", .05, priceType = 'bid_price')
        r.order_sell_crypto_by_quantity("BCH", .05, priceType = 'ask_price')
        print("Bought and sold")
    
    if (bid_price > ask_price):
        r.order_buy_crypto_by_quantity("BCH", .05, priceType = 'ask_price')
        r.order_sell_crypto_by_quantity("BCH", .05, priceType = 'bid_price')
        print("Bought and sold")
    sleep(15)
    print('\n')