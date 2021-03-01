import requests, json
import robin_stocks as r
import analysis as a
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

# note: this seems unchangable, but the API provides data for the "close" -- the default in Binance's chart is set to "open", so you will see a discripancy unless you adjust the settings on the chart

def getPwd():
    return os.environ['RH_PWD']

def RSI(ticker='BTC', backtrack=0, api = 1):
    # Define indicator
    indicator = "rsi"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    secret = a.getAPIKey(api)
    
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

    return round(float(result['value']), 4)

def stochRSI(ticker='BTC', backtrack=0, api = 1):
    # Define indicator
    indicator = "stochf"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    secret = a.getAPIKey(api)
    
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

    return round(float(result['valueFastK']), 4)

# Average Directional Index
def ADX(ticker='BTC', backtrack=0, api = 1):
    # Define indicator
    indicator = "adx"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    secret = a.getAPIKey(api)
    
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

    return round(float(result['value']), 4)

# Ultimate Oscillator
def ultOSC(ticker='BTC', backtrack=0, api = 1):
    # Define indicator
    indicator = "ultosc"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    secret = a.getAPIKey(api)
    
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

    return round(float(result['value']), 4)

# directional movement index
def DMI(ticker='BTC', val = 'plusdi', backtrack=0, api = 1):
    # Define indicator
    indicator = "dmi"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    secret = a.getAPIKey(api)
    
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
    
    return round(float(result[val]), 4)

# Rate of Change Indicator
def ROC(ticker='BTC', backtrack=0, api=1):
    # Define indicator
    indicator = "roc"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

     # get API key
    secret = a.getAPIKey(api)
    
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

    return round(float(result['value']), 4)

def direction(ticker='BTC', backtrack = 0, api = 1):
    # Define indicator
    indicator = "pd"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"

    # get API key
    secret = a.getAPIKey(api)
    
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

    return round(float(result['value']), 4)

def price(ticker='BTC'):
    return float(r.crypto.get_crypto_quote(ticker)['ask_price'])

def buy(ticker, amountInAsset):
    r.order_buy_crypto_by_quantity(ticker, amountInAsset)
    print("Bought")

def sell(ticker, amountInAsset):
    r.order_sell_crypto_by_quantity(ticker, amountInAsset)
    print("Sold")

def login():
    # Logs into Robinhood
    pwd = getPwd()
    r.login(username="nicktalwar",
         password=pwd,
         expiresIn=86400,
         by_sms=True)
    
def dataPoints(ticker='BTC', backTrack=0, API = 1):
    success = False
    while not success:
        try:
            success = True
            data = getData(ticker, backTrack, API)
        except:
            success = False
            if (API == 1):
                API = 2
            elif (API == 2):
                API = 3
            elif (API == 3):
                API = 1
    print("Ticker: " + ticker)
    return data

def getData(ticker='BTC', backTrack=0, API = 1):
    return [RSI(ticker, backtrack = backTrack, api = API), ultOSC(ticker, backtrack = backTrack, api = API), stochRSI(ticker, backtrack = backTrack, api = API), DMI(ticker, val = 'plusdi', backtrack = backTrack, api = API), DMI(ticker, val = 'minusdi', backtrack = backTrack, api = API), ROC(ticker, backtrack = backTrack, api = API), direction(ticker, backtrack = backTrack, api = API), price(ticker)]

def dataPointsTwo(ticker='BTC', backTrack=10):
    print(ticker)
    return [RSI(ticker, backTrack), ultOSC(ticker, backTrack), stochRSI(ticker, backTrack), DMI(ticker, 'plusdi', backTrack), DMI(ticker, 'minusdi', backTrack), ROC(ticker, backTrack), ADX(ticker, backTrack), direction(ticker, backTrack), priceTwo(ticker, backTrack), priceTwo(ticker, 0)]