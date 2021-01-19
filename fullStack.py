from training import train
#from test import test
from time import sleep
from controller2 import cycle

steps = 2
time = int(input("How long between each cycle? "))
amount = int(input("Amount: "))

for i in range(int(input("Cycles: "))):
    
    """train(steps, [], 0, steps, 5)
    print("Added " + str(steps) + " rows to the dataset")"""
    cycle(steps+3, 0, 0, 0, buy, steps+3, time, amount)
    print("Cycled " + str(steps+3) + " times")
    #results = test(5)
    #print("The program results were: " + str(results) + "%")

    """if (i > 0):
        print(oldResults)
        improvement = (results - oldResults)/ oldResults
        improvement *= 100
        print("Up " + str(improvement) + " from the last cycle")"""

    #oldResults = results
    print('\n')
    sleep(1200)

print("Loop complete")