from regression import predict

def stratAI():
    # average time per generated prediction using a 1660 ti and a 10th gen intel i5: .38872 seconds

    # total votes for buying and selling
    buyVotes = 0
    sellVotes = 0
    
    # generates 125 predictions
    for i in range(5):
        sell = []
        buy = []
        for x in range(25):
            results = predict()
            if results[0] == 0:
                sell.append(results[1])
            else:
                buy.append(results[1])
        
        if (average(sell) > average(buy)):
            sellVotes += 1
        else:
            buyVotes += 1
    
    if (buyVotes == 5):
        print(buyVotes / 5)
        return 1
    elif (sellVotes > buyVotes):
        print(-1 * (sellVotes / 5))
        return 0
    return "HOLD"

def stratAITwo(verbose = True):
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

    if (verbose):
        print("Model accuracy: " + str(best*100) + "%")

    return prediction

# This is used so that I only need to change the code in one place when I change the strategy.
def strat(indicators = [], verbose = False):
    return stratAI()