import requests
import robin_stocks as r
import analysis as a
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

# note: this seems unchangable, but the API provides data for the "close" -- the default in Binance's chart is set to "open", so you will see a discripancy unless you adjust the settings on the chart

interval = '5m'

def getPwd():
    return os.environ['RH_PWD']

def login():
    # Logs into Robinhood
    pwd = getPwd()
    r.login(username="nicktalwar",
         password=pwd,
         expiresIn=86400,
         by_sms=True)
        
    print("Successfully logged in to Robinhood API")

def RSI(ticker='BTC', api = 1):
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
        'optInTimePeriod':'10'      
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    try:
        return round(float(result['value']), 4)
    except:
        api = a.shuffleKeys(api)

        return RSI(ticker, api)

def stochRSI(ticker='BTC', api = 1):
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
        'optInTimePeriod':'12'      
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    try:
        return round(float(result['valueFastK']), 4)
    except:
        api = a.shuffleKeys(api)

        return stochRSI(ticker, api)

# Average Directional Index
def ADX(ticker='BTC', api = 1):
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
        'interval': '1m'
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    try:
        return round(float(result['value']), 4)
    except:
        api = a.shuffleKeys(api)

        return ADX(ticker, api)

# Ultimate Oscillator
def ultOSC(ticker='BTC', api = 1):
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
        'interval': '1m'
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json()

    try:
        return round(float(result['value']), 4)
    except:
        api = a.shuffleKeys(api)

        return ultOSC(ticker, api)
        

# directional movement index
def DMI(ticker='BTC', val = 'plusdi', api = 1):
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
        'interval': '1m'
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 
    
    try:
        return round(float(result[val]), 4)
    except:
        api = a.shuffleKeys(api)

        return DMI(ticker, val, api)
    
# Rate of Change Indicator
def ROC(ticker='BTC', api=1):
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
        'interval': '1m'
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json()

    try:
        return round(float(result['value']), 4)
    except:
        api = a.shuffleKeys(api)

        return ROC(ticker, api)

def direction(ticker='BTC', api = 1):
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
        'interval': '1m'
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    try:
        return round(float(result['value']), 4)
    except:
        api = a.shuffleKeys(api)

        return direction(ticker, api)

def price(ticker='BTC'):
    login()
    return float(r.crypto.get_crypto_quote(ticker)['ask_price'])

def buy(ticker, amountInAsset):
    r.order_buy_crypto_by_quantity(ticker, amountInAsset)

def sell(ticker, amountInAsset):
    r.order_sell_crypto_by_quantity(ticker, amountInAsset)

def SymbolToData(symbol, ticker, API):
    conversions = {
        "RSI": RSI(ticker, api = API),
        "ULTOSC": ultOSC(ticker, api = API),
        "STOCHRSI": stochRSI(ticker, api = API),
        "+DI": DMI(ticker, val = 'plusdi', api = API),
        "-DI": DMI(ticker, val = 'minusdi', api = API),
        "ROC": ROC(ticker, api = API),
        "PD": direction(ticker, api = API)
    }

    return conversions[symbol]

def getData(symbols=a.getHeaders(), ticker = 'BTC', API = 1):
    if ("CHANGE" in symbols):
        symbols.remove("CHANGE")
    
    data = []

    for symbol in symbols:
        data.append(SymbolToData(symbol, ticker, API))

    return data

def dataPoints(ticker='BTC', API = 1, symbols = a.getHeaders()):
    success = False

    while not success:
        try:
            success = True
            data = getData(symbols, ticker, API)
        except:
            success = False
            
            key = a.shuffleKeys(key)
    print("Ticker: " + ticker)
    return data