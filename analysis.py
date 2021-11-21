from csv import *

# Function for appending values to a CSV files (from a list)
def append_list_as_row(file_name, list_of_elem, action):
    # Open file in append mode
    with open(file_name, action, newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj, lineterminator='\n')
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
    write_obj.close()

def store_csv_indicators(dp, file, add="null"):
    if (add != "null"):
        dp.append(add)

    append_list_as_row(file, dp, 'a')

def percentDiff(newVal, oldVal):
    diff = newVal - oldVal
    diff *= 100
    diff /= oldVal
    return diff

# This stragegy does the following:
# 1. Checks to ensure the RSI is in a valid range
# 2. Ensures that the asset was not recently in an uptrend (that may be ending)
# 3. Checks to see if the exponential moving average is more than the moving average
# Indicators: RSI, MA, EMA
def complexStrat(indicators):
    rsi = indicators[0]
    ma = indicators[1]
    ema = indicators[2]

    # I have noticed that the ema is greater than the ma at the end of a bull run
    # if the ema is less than the ma, it may be the beginning of a bull run
    if (rsi > 65):
        return False
    
    if (rsi < 35):
        return True
    
    if (rsi > 55 and ma < ema):
        return False
    
    if (rsi < 45 and ema < ma):
        return True
    
    if (rsi > 60 and ma < 0 and ema < 0):
        return False
    
    if (ma > 0 and ema > 0 and rsi < 35):
        return True
    
    return "HOLD"

def getHeaders():
    # Ultosc is better in sideways markets, RSI is better in trending markets
    return ["RSI", "STOCHRSI", "+DI", "-DI", "ROC", "PD", "CHANGE"]

def showIndicators(indicators):
    headers = getHeaders()
    headers.remove("CHANGE")
    for i in range (len(headers)):
        print(str(headers[i]) + ": " + str(indicators[i]))

def APIkey():
    return 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70'

def APIKeyTwo():
    return 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im0xM3NjMG1yYWlkZUBnbWFpbC5jb20iLCJpYXQiOjE2MTI5MDMxMTMsImV4cCI6NzkyMDEwMzExM30.N-jdpAQtZJsGOJk_R63SiDCso3qHhho8oB3I1qfEuRM'

def APIKeyThree():
    return 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRhcmswbmNvZGVyQGdtYWlsLmNvbSIsImlhdCI6MTYxNDU2Mzc0NCwiZXhwIjo3OTIxNzYzNzQ0fQ.yHWO1Y3p-NSUWy_N0DwGIiqC9EtjrmB2yYHdz-AWUuQ'

def APIKeyFour():
    return 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MzYyMjA0ODYsImV4cCI6Nzk0MzQyMDQ4Nn0.uwonW4C7Zknvw75MRUq34by1Zakj_AGoL-jIbDM6V-M'

def getAPIKey(id):
    keys = {
        1:APIkey(),
        2:APIKeyTwo(),
        3:APIKeyThree(),
        4:APIKeyFour()
    }
    return keys[id]

def shuffleKeys(key):
    key += 1

    if (key > 4):
        key = 1
    
    return key

def average(list):
    if (len(list) == 0):
        return 0
    return sum(list) / len(list)