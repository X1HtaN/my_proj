from random import random, randrange


ready = input("ready?\n")

if (ready == "yes"):
    activ = True
else:
    activ = False

def getNum(servNum):
    servNum = randrange(11)
    return servNum

def congrac():
    print("server Number Ready\n")
    print("number 1 - 10\n")

servNum = getNum(0)

congrac()

while activ:

    userNum = int(input())

    if (servNum == userNum):
        print("you win\n")
        print("it's", servNum, "\n")  
        congrac()
        servNum = getNum(0)
        continue
    elif(servNum > userNum):
        print("the number is greater\n")
    elif(servNum < userNum):
        print("number less\n")