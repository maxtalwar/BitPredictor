import dataScrape as d
import analysis as a
from time import sleep
import robin_stocks as r
from datetime import datetime

d.login()

# defines starting variables

ticker = str(input("Ticker: "))

startingCash = float(input("How much cash in your account? "))

amountInUSD = float(input("Trade amount (USD): "))

cycles = int(input("How many cycles? "))

amountInAsset = round(amountInUSD/d.price(ticker), 5)

owned = False

api = 1

headers = a.getHeaders()

print("Asset amount traded on: " + str(amountInAsset) + " " + ticker)

# iterates a certain amount of times
for i in range (cycles):
	print('\n')

	# displays the time
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print("Current Time =", current_time)

	# gets the data
	indicators = d.dataPoints(ticker, api)

	# adds a comma value to the data so it works with a csv file
	indicators.append("")

	# adds the predict data to a csv file
	a.append_list_as_row('predict.csv', headers, 'w')
	a.append_list_as_row("predict.csv", indicators, 'a')
	a.showIndicators(indicators)

	# creates the model and the prediction
	predict = a.strat(indicators, verbose = False)

	# shows the prediction
	if (predict == 1):
		print("Predicted action: BUY")
	elif (predict == 0):
		print("Predicted action: SELL")
	else:
		print("Predicted action: HOLD")

	# gets the price
	try:
		price = d.price(ticker)
	except:
		d.login()
		price = d.price(ticker)

	# shows the price and holdings
	print("Price: $" + str(price))
	print("Owned: " + str(owned))

	# chekcs to see if the bot should buy
	if (predict == True and not owned and indicators[0] <= 60):
		amountInAsset = round(amountInUSD/price, 5)
		owned = True
		d.buy(ticker, amountInAsset)
		print("Bought at: $" + str(price))
	
	# checks to see if the bot should sell
	elif (predict == False and owned):
		profit = amountInAsset*price - amountInUSD
		print("Profit: $" + str(profit))
		d.sell(ticker, amountInAsset)
		amountInAsset = 0
		owned = False
	
	# checks to see if the bot should take profits
	elif (owned):
		profit = amountInAsset*price - amountInUSD
		if (profit >= .25):
			owned = False
			d.sell(ticker, amountInAsset)
			print("Sold Asset (Taking gains)")
			print("Profit: $" + str(profit))
		elif (profit <= -.5):
			owned = False
			d.sell(ticker, amountInAsset)
			print("Sold Asset (Stopping Losses)")
			print("Profit: $" + str(profit))
	
	if (owned):
		for i in range(4):
			sleep(150)
			price = d.price(ticker)
			profit = amountInAsset*price - amountInUSD
			if (profit >= .3 or profit <= -.5):
				print('\n')
				owned = False
				d.sell(ticker, amountInAsset)
				print("Sold Asset (Taking gains / stop loss)")
				print("Sold at: " + str(price))
				print("Profit: $" + str(amountInAsset*d.price(ticker) - amountInUSD))
				break
	else:
		sleep(600)

print('\n')

# sells all assets at the end
if (owned):
    input("Please note: there is still " + str(amountInAsset) +  ticker + " in the account that has not been sold. Hit enter when you have successfully sold this amount")

sleep(180)

cash = r.account.load_phoenix_account(info=None)['account_buying_power']['amount']

profit = float(cash) - startingCash

print("Current Cash: $" + str(cash))

print("Starting Cash: $" + str(startingCash))

print("You profited: $"  + str(profit) + " over the course of " + str(cycles*10) + " minutes")

print("This was an average profit of $" + str(profit * 6 / cycles) + " per hour")