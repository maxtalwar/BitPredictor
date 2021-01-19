# Setup the data
import turicreate as tc

def predict (train = 'prices.csv', predict='predict.csv'):
    """train_data =  tc.SFrame.read_csv(train, verbose = False)

    predict_data = tc.SFrame.read_csv(predict, verbose = False)

    # Selects the best model based on your data.
    # boosted_tree_regression seems to be the best type of regression for this data
    model = tc.logistic_classifier.create(train_data, target='CHANGE', features=['RSI', 'MA', 'EMA'], validation_set='auto', verbose=False)

    # Make predictions and evaluate results.
    predictions = model.predict(predict_data)
    results = model.evaluate(train_data)

    print(results)"""

    data =  tc.SFrame(train)

    # Select the best model based on your data.
    model = tc.regression.create(data, target='CHANGE', features=['RSI', 'MA', 'EMA'])

    # Make predictions and evaluate results.
    predictions = model.predict(data)
    results = model.evaluate(data)

    print(results)

    if (len(predictions) == 1):
        return predictions[0]
    else:
        return predictions
