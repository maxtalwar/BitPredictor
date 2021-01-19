from regression import predict
from csv import *
import turicreate
# 5, 2
# 4, 3


# Function for appending values to a CSV files (from a list)
def append_list_as_row(file_name, list_of_elem, action):
    # Open file in append mode
    with open(file_name, action, newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj, lineterminator='\n')
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
    write_obj.close()

def store_csv_indicators(dp, time, file, add=""):
    dp.append(float(time))
    dp.append(add)

    append_list_as_row(file, dp, 'a')


def crossover(oldOne, newOne):
    if (oldOne <= 0):
        if (newOne > 0):
            return True

    return False

def increase(newVal, oldVal):
    if ((newVal > oldVal) and newVal > 0):
        return True
    return False

def direction(newVal, oldVal):
    return newVal > oldVal

def percentDiff(newVal, oldVal):
    diff = newVal - oldVal
    diff *= 100
    diff /= oldVal
    return diff

def appreciateRSI(rsi):
    return (rsi < 65)

# This stragegy does the following:
# 1. Checks to ensure the RSI is in a valid range
# 2. Ensures that the asset was not recently in an uptrend (that may be ending)
# 3. Checks to see if the exponential moving average is more than the moving average
# Indicators: RSI, MA, EMA
def complexStrat(indicators, oldIndicators=[]):
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

def showIndicators(indicators):
    print("Current RSI: " + str(indicators[0]))

    print("Current MA: " + str(indicators[1]))

    print("Current EMA: " + str(indicators[2]))
    
    

"""def findSell(indicators, oldIndicators):
    rsi = indicators[0]
    macd = indicators[1]
    ma = indicators[2]
    ema = indicators[3]

    if (rsi > 65 and ma > ):"""
        
    
def stratAI():
    return (predict() == 1)

# This is used so that I only need to change the code in one place when I change the strategy.
def strat(indicators):
    return stratAI()