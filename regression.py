# Setup the data
import turicreate as tc
import analysis as a

def predict (train = 'prices.csv', predict ='predict.csv', features = []):

    predict_data = tc.SFrame.read_csv(predict, header=True, verbose = False)

    # Load the data
    data =  tc.SFrame.read_csv(train, header=True, verbose=False)

    train_data, test_data = data.random_split(0.8)

    #train_data = tc.SFrame.read_csv(train, header=True, verbose = False)

    # 'RSI', 'ULTOSC', 'STOCHRSI', '+DI', '-DI', 'ROC', 'PD', 'CHANGE'

    if (len(features) > 0):
        f = features
    else:
        f = a.setHeaders()
        f.remove("CHANGE")

    # Selects the best model based on your data.
    # boosted_trees_classifier seems to be the best type of regression for this data
    # classifier model options: boosted_trees_classifier, random_forest_classifier, decision_tree_classifier, logistic_classifier, svm_classifier
    #model = tc.boosted_trees_classifier.create(train_data, target='CHANGE', features=f, validation_set='auto', max_depth = 10, verbose = False)

    # The above model has a limit on depth and iterations - it might be best to restrict that
    # the performance of max_iteration of 50 seems to be on par with the default values
    # it's unclear what gives the best performance for max_depth right now

    # Make predictions and evaluate results.
    model = tc.boosted_trees_classifier.create(train_data, target='CHANGE', features=f, validation_set='auto', max_depth = 10, verbose = False)

    predictions = model.predict(predict_data)

    results = model.evaluate(test_data)['accuracy']

    info = [predictions[0], results]

    # Save the data for future use
    #model.save('classifier.model')

    return info

    """if (len(predictions) == 1):
        return predictions[0]
    else:
        return predictions"""
