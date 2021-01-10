import requests, json
import robin_stocks as r
import analysis as a
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# Logs into Robinhood
login = r.login(username="maxnmtalwar@gmail.com",
         password="8#k5uqP9NG@n",
         expiresIn=86400,
         by_sms=True)

def MACD():
    # Define indicator
    indicator = "macdfix"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70',
        'exchange': 'binance',
        'symbol': 'BCH/USDT',
        'interval': '5m'
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 
    
    #print(result)
    return round(float(result["valueMACDHist"]), 4)

def RSI():
    # Define indicator
    indicator = "rsi"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70',
        'exchange': 'binance',
        'symbol': 'BCH/USDT',
        'interval': '5m'
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    #print(result)
    return round(float(result['value']), 4)

def MA():
    # Define indicator
    indicator = "ma"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70',
        'exchange': 'binance',
        'symbol': 'BCH/USDT',
        'interval': '5m'
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    #print(result)
    return round(float(result['value']), 4)

def EMA():
    # Define indicator
    indicator = "ema"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70',
        'exchange': 'binance',
        'symbol': 'BCH/USDT',
        'interval': '5m'
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    #print(result)
    return round(float(result['value']), 4)

def price(ticker = "BCH", priceType = 'ask_price'):
    return float(r.crypto.get_crypto_quote("ETH", priceType))

def buy(amountInAsset, ticker = "BCH"):
    r.order_buy_crypto_by_quantity(ticker, amountInAsset, priceType = 'bid_price')

def sell(amountInAsset, ticker = "BCH"):
    r.order_sell_crypto_by_quantity(ticker, amountInAsset, 'ask_price')

def dataPoints():
    ma = round(a.percentDiff(MA(), price()), 4)
    ema = round(a.percentDiff(EMA(), price()), 4)
    return [RSI(), MACD(), ma, ema]