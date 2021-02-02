# Setup the data
import turicreate as tc

def predict (train = 'prices.csv', predict ='predict.csv', test = 'test.csv'):
    train_data =  tc.SFrame.read_csv(train, header=True, verbose = False)

    predict_data = tc.SFrame.read_csv(predict, header=True, verbose = False)

    #test_data = tc.SFrame.read_csv(test, header=True, verbose = False)

    #print(predict_data)

    # Selects the best model based on your data.
    # boosted_trees_classifier seems to be the best type of regression for this data
    # classifier model options: boosted_trees_classifier, random_forest_classifier, decision_tree_classifier, logistic_classifier, svm_classifier, nearest_neighbor_classifier
    model = tc.boosted_trees_classifier.create(train_data, target='CHANGE', features=['RSI', 'MA', 'EMA', 'MACD', 'ULTOSC', 'STOCHRSI', '+DI', '-DI', 'ROC'], validation_set='auto', verbose=False)

    # Make predictions and evaluate results.
    #predictions = model.predict(predict_data)

    results = model.evaluate(train_data)

    print(results)

    if (len(predictions) == 1):
        return predictions[0]
    else:
        return predictions
