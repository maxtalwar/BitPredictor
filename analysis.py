from regression import predict
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

def setHeaders():
    return ["RSI", "ULTOSC", "STOCHRSI", "+DI", "-DI", "ROC", "PD", "CHANGE"]

def showIndicators(indicators):
    headers = setHeaders()
    headers.remove("CHANGE")
    for i in range (len(headers)):
        print(str(headers[i]) + ": " + str(indicators[i]))

def APIkey():
    return 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG5sZWFmZXIwNUBnbWFpbC5jb20iLCJpYXQiOjE2MDgwNzc2ODUsImV4cCI6NzkxNTI3NzY4NX0.mtwEhqsNv0E76gXPHtdNn4GHmg8XkQp2S8G988pyA70'

def APIKeyTwo():
    return 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im0xM3NjMG1yYWlkZUBnbWFpbC5jb20iLCJpYXQiOjE2MTI5MDMxMTMsImV4cCI6NzkyMDEwMzExM30.N-jdpAQtZJsGOJk_R63SiDCso3qHhho8oB3I1qfEuRM'
    
def stratAI(verbose = True):
    best = 0
    prediction = 0

    for i in range(20):
        # results[0] is the predicted value, results[1] is the accuracy of that model
        results = predict()
        if (results[1] > best):
            best = results[1]
            prediction = results[0]
        if (verbose):
            print(results[1])
    print(str(results[1]) + ":" + str(results[0]))

    print("Current model accuracy: " + str(best*100) + "%")

    return [prediction, best]

# This is used so that I only need to change the code in one place when I change the strategy.
def strat(indicators, verbose = False):
    return stratAI(verbose)

def average(list):
    return sum(list) / len(list)