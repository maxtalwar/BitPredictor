import turicreate as tc

data =  tc.SFrame.read_csv("experiment2.csv")

predict_data = tc.SFrame.read_csv("predict.csv")

# Selects the best model based on your data.
model = tc.regression.create(data, target='CHANGE',features=['RSI', 'MA', 'EMA'])

# Make predictions and evaluate results.
predictions = model.predict(predict_data)
results = model.evaluate(data)

print(predictions)