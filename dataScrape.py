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
def MACD(ticker='BTC', backtrack=0):
    # Define indicator
    indicator = "macd"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70',
        'exchange': 'binance',
        'symbol': ticker + '/USDT',
        'interval': '1m',
        'backtrack':backtrack,
        'optInFastPeriod':12,
        'optInSlowPeriod':26,
        'optInSignalPeriod':9
        } 
    
    # Send get request and save the response as response object 
    response = requests.get(url = endpoint, params = parameters)
    
    # Extract data in json format 
    result = response.json() 

    # Print result
    #print(result)
    return round(float(result["valueMACDHist"]), 4)

def macds(ticker='BTC'):
    macds = [MACD(ticker, 2), MACD(ticker, 1)]
    if (macds[0] < 0 and macds[1] > 0):
        return 1
    elif (macds[0] > 0 and macds[1] < 0):
        return -1
    
    return 0


def RSI(ticker='BTC', backtrack=0):
    print(ticker)

    # Define indicator
    indicator = "rsi"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70',
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

    # Print result
    #print(result)
    return round(float(result['value']), 4)

def stochRSI(ticker='BTC', backtrack=0):
    # Define indicator
    indicator = "stochf"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70',
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
    return round(float(result['valueFastK']), 4)

def MA(ticker='BTC', backtrack=0):
    # Define indicator
    indicator = "ma"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70',
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
    return round(float(result['value']), 4)

def EMA(ticker='BTC', backtrack=0):
    # Define indicator
    indicator = "ema"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70',
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
    return round(float(result['value']), 4)

# Average Directional Index
def ADX(ticker='BTC', backtrack=0):
    # Define indicator
    indicator = "adx"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70',
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
    return round(float(result['value']), 4)

# Ultimate Oscillator
def ultOSC(ticker='BTC', backtrack=0):
    # Define indicator
    indicator = "ultosc"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70',
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
    return round(float(result['value']), 4)


# directional movement index
def DMI(ticker='BTC', backtrack=0, val = 'plusdi'):
    # Define indicator
    indicator = "dmi"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70',
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
    return round(float(result[val]), 4)

# Rate of Change Indicator
# directional movement index
def ROC(ticker='BTC', backtrack=0):
    # Define indicator
    indicator = "roc"
    
    # Define endpoint 
    endpoint = f"https://api.taapi.io/{indicator}"
    
    # Define a parameters dict for the parameters to be sent to the API 
    parameters = {
        'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70',
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
    
def dataPoints(ticker='BTC', backTrack=0):
    print(ticker)
    ma = round(a.percentDiff(MA(ticker, backTrack), price(ticker)), 4)
    ema = round(a.percentDiff(EMA(ticker, backTrack), price(ticker)), 4)
    return [RSI(ticker), ma, ema, macds(ticker), ultOSC(ticker), stochRSI(ticker), DMI(ticker = ticker, val = 'plusdi'), DMI(ticker = ticker, val = 'minusdi'), ROC(ticker)]