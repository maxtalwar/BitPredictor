from regression import predict
from csv import *
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
# Indicators: RSI, MACD, MA, EMA
def complexStrat(indicators, oldIndicators):
    rsi = indicators[0]
    macd = indicators[1]
    ma = indicators[2]
    ema = indicators[3]

    if (appreciateRSI(rsi)):
        # makes sure that the moving average and the macd are less than 0 
        # if the MA and the MACD are more than 0, they may have just finished an uptrend
        if (oldIndicators[1] < 0 and macd > 0):
            return True
        if (oldIndicators[1] > 0 and macd < 0):
            return False
        
        if (oldIndicators[2] > 0 and ma < 0):
            return True
        if (oldIndicators[2] < 0 and ma > 0):
            return False
        
        if ((macd - oldIndicators[1]) > (oldIndicators[1]/2)):
            return True
        if (macd < oldIndicators[1]):
            return False
        # I have noticed that if the EMA is more than the MA, that is the mark of the end of a downward trend
        #if (direction())
        return "HOLD"
    
    return False

"""def findSell(indicators, oldIndicators):
    rsi = indicators[0]
    macd = indicators[1]
    ma = indicators[2]
    ema = indicators[3]

    if (rsi > 65 and ma > ):"""
        
    
def stratAI():
    return (predict() == 1)
