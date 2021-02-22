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

# note: this seems unchangable, but the API provides data for the "close" -- the default in Binance's chart is set to "open", so you will see a discripancy unless you adjust the settings on the chart

def RSI(ticker='BTC', backtrack=0, api = 0):

    # Define indicator
    indicator = "rsi"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    if (api == 0):
        secret = a.APIkey()
    else:
        secret = a.APIKeyTwo()
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': secret,
        'exchange': 'binance',
        'symbol': ticker + '/USDT',
        'interval': '1m',
        'optInTimePeriod':'10',
        'backtrack':backtrack        
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    # Print result
    #print(result)
    try:
        return round(float(result['value']), 4)
    except:
        print(result)
        return round(float(result['value']), 4)

def stochRSI(ticker='BTC', backtrack=0, api = 0):
    # Define indicator
    indicator = "stochf"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    if (api == 0):
        secret = a.APIkey()
    else:
        secret = a.APIKeyTwo()
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': secret,
        'exchange': 'binance',
        'symbol': ticker + '/USDT',
        'interval': '1m',
        'optInTimePeriod':'12',
        'backtrack':backtrack        
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    #print(result)
    try:
        return round(float(result['valueFastK']), 4)
    except:
        print(result)
        return round(float(result['valueFastK']), 4)

def MA(ticker='BTC', backtrack=0, api = 0):
    # Define indicator
    indicator = "ma"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    if (api == 0):
        secret = a.APIkey()
    else:
        secret = a.APIKeyTwo()
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': secret,
        'exchange': 'binance',
        'symbol': ticker + '/USDT',
        'interval': '1m',
        'backtrack':backtrack
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    # Print result
    #print(result)
    try:
        return round(float(result['value']), 4)
    except:
        print(result)
        return round(float(result['value']), 4)

def EMA(ticker='BTC', backtrack=0, api = 0):
    # Define indicator
    indicator = "ema"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    if (api == 0):
        secret = a.APIkey()
    else:
        secret = a.APIKeyTwo()
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': secret,
        'exchange': 'binance',
        'symbol': ticker + '/USDT',
        'interval': '1m',
        'backtrack':backtrack
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    # Print result
    try:
        return round(float(result['value']), 4)
    except:
        print(result)
        return round(float(result['value']), 4)

# Average Directional Index
def ADX(ticker='BTC', backtrack=0, api = 0):
    # Define indicator
    indicator = "adx"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    if (api == 0):
        secret = a.APIkey()
    else:
        secret = a.APIKeyTwo()
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': secret,
        'exchange': 'binance',
        'symbol': ticker + '/USDT',
        'interval': '1m',
        'backtrack':backtrack
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    # Print result
    try:
        return round(float(result['value']), 4)
    except:
        print(result)
        return round(float(result['value']), 4)

# Ultimate Oscillator
def ultOSC(ticker='BTC', backtrack=0, api = 0):
    # Define indicator
    indicator = "ultosc"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    if (api == 0):
        secret = a.APIkey()
    else:
        secret = a.APIKeyTwo()
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': secret,
        'exchange': 'binance',
        'symbol': ticker + '/USDT',
        'interval': '1m',
        'backtrack':backtrack
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    # Print result
    try:
        return round(float(result['value']), 4)
    except:
        print(result)
        return round(float(result['value']), 4)

# directional movement index
def DMI(ticker='BTC', val = 'plusdi', backtrack=0, api = 0):
    # Define indicator
    indicator = "dmi"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    if (api == 0):
        secret = a.APIkey()
    else:
        secret = a.APIKeyTwo()
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': secret,
        'exchange': 'binance',
        'symbol': ticker + '/USDT',
        'interval': '1m',
        'backtrack':backtrack
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    try:
    # Print result
        return round(float(result[val]), 4)
    except:
        print(result)
        return round(float(result[val]), 4)

# Rate of Change Indicator
# directional movement index
def ROC(ticker='BTC', backtrack=0, api=0):
    # Define indicator
    indicator = "roc"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

     # get API key
    if (api == 0):
        secret = a.APIkey()
    else:
        secret = a.APIKeyTwo()
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': secret,
        'exchange': 'binance',
        'symbol': ticker + '/USDT',
        'interval': '1m',
        'backtrack':backtrack
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    try:
        return round(float(result['value']), 4)
    except:
        print(result)
        return round(float(result['value']), 4)

def price(ticker='BTC'):
    return float(r.crypto.get_crypto_quote(ticker)['ask_price'])

# gets the average price of the most recent candle
def priceTwo(ticker = 'BTC', backtrack=0, api= 0):
    # Define indicator
    indicator = "typprice"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    if (api == 0):
        secret = a.APIkey()
    else:
        secret = a.APIKeyTwo()
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': secret,
        'exchange': 'binance',
        'symbol': ticker + '/USDT',
        'interval': '1m',
        'backtrack':backtrack
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    try:
        return round(float(result['value']), 4)
    except:
        print(result)
        return round(float(result['value']), 4)

def priceChange(ticker='BTC', backtrack = 10):
    prices = [priceTwo(ticker, backtrack), priceTwo(ticker, 0)]
    oldPrice = prices[0]
    price = prices[1]
    print(oldPrice)
    print(price)
    if (price > oldPrice):
        return 1
    return 0

def direction(ticker='BTC', backtrack = 0, api = 0):
    # Define indicator
    indicator = "pd"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    if (api == 0):
        secret = a.APIkey()
    else:
        secret = a.APIKeyTwo()
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': secret,
        'exchange': 'binance',
        'symbol': ticker + '/USDT',
        'interval': '1m',
        'backtrack':backtrack
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    try:
        return round(float(result['value']), 4)
    except:
        print(result)
        return round(float(result['value']), 4)

def buy(ticker, amountInAsset):
    r.order_buy_crypto_by_quantity(ticker, amountInAsset)
    print("Bought")

def sell(ticker, amountInAsset):
    r.order_sell_crypto_by_quantity(ticker, amountInAsset)
    print("Sold")

def login():
    # Logs into Robinhood
    r.login(username="maxnmtalwar@gmail.com",
         password="8#k5uqP9NG@n",
         expiresIn=86400,
         by_sms=True)
    
def dataPoints(ticker='BTC', backTrack=0, API = 0):
    print(ticker)
    ma = round(a.percentDiff(MA(ticker), price(ticker)), 4)
    ema = round(a.percentDiff(EMA(ticker), price(ticker)), 4)
    return [RSI(ticker, backtrack = backTrack, api = API), ultOSC(ticker, backtrack = backTrack, api = API), stochRSI(ticker, backtrack = backTrack, api = API), DMI(ticker, val = 'plusdi', backtrack = backTrack, api = API), DMI(ticker, val = 'minusdi', backtrack = backTrack, api = API), ROC(ticker), direction(ticker, backtrack = backTrack, api = API), price(ticker)]

def dataPointsTwo(ticker='BTC', backTrack=10):
    print(ticker)
    ma = round(a.percentDiff(MA(ticker, backTrack), priceTwo(ticker, backTrack)), 4)
    ema = round(a.percentDiff(EMA(ticker, backTrack), priceTwo(ticker, backTrack)), 4)
    return [RSI(ticker, backTrack), ultOSC(ticker, backTrack), stochRSI(ticker, backTrack), DMI(ticker, 'plusdi', backTrack), DMI(ticker, 'minusdi', backTrack), ROC(ticker, backTrack), ADX(ticker, backTrack), direction(ticker, backTrack), priceTwo(ticker, backTrack), priceTwo(ticker, 0)]