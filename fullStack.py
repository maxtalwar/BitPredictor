import emailClient as email
import test as t
import training
from time import sleep

for i in range(5):
    print("MAIN Cycle: " + str(i+1))
    accuracy = t.test(20, 10, 10)
    print("Accuracy: " + str(accuracy))
    message = email.createMessage("BitTrader", str(accuracy))

    email.sendEmail(message)

    #steps = training.train(12, [], 0, 12, 10, [])
    #print("Added " + str(steps) + " rows to the dataset")
    print('\n')
    sleep(300)