from argparse import ArgumentError
from ast import Break, While
import random


print("Stone Paper Scissors")

while (True):

    userValue = None
    startServerValue = None
    endServerValue = None

    if(input ("ready?\n") == "no"):
        break

    userValue = input("value? (stone / scissors / paper)\n")

    if (userValue == "stone"):
        userValue = 1
    elif(userValue == "scissors"):
        userValue = 2
    elif(userValue == "paper"):
        userValue = 3
    else:
        print("not defind")
        continue 

    startServerValue = random.randint(0, 4)

    if (startServerValue == 1):
        endServerValue = "stone"

    elif (startServerValue == 2):
        endServerValue = "scissors"

    else:
        endServerValue = "paper"

    if  (userValue == endServerValue):
            print("ServerValue:", endServerValue)
            print("draw")
            continue

    if (userValue == 1):
        if (endServerValue == "scissors"):
            print("ServerValue:", endServerValue)
            print("win")
            continue
        elif(endServerValue == "paper"):
            print("ServerValue:", endServerValue)
            print("lose")
            continue

    elif (userValue == 2):
        if (endServerValue == "stone"):
            print("ServerValue:", endServerValue)
            print("lose")
            continue
        elif(endServerValue == "paper"):
            print("ServerValue:", endServerValue)
            print("win")
            continue

    elif (userValue == 3):
        if(endServerValue == "stone"):
            print("ServerValue:", endServerValue)
            print("win")
            continue
        elif(endServerValue == "scissors"):
            print("ServerValue:", endServerValue)
            print("lose")
            continue
