from random import Random


import random

def playerVariables():
    playerVariable = input("stone / scissors / paper\n")
    if playerVariable == "end": return False
    return playerVariable

def playerVariableCheckDraw(playerVariable, compVariable):
    if playerVariable != compVariable:
        if playerVariable == "stone": playerVariableCheckStone(compVariable)
        if playerVariable == "scissors": playerVariableCheckScissors(compVariable)
        if playerVariable == "paper": playerVariableCheckPaper(compVariable)
    else:
        print("draw comp:", compVariable)

def playerVariableCheckStone(compVariable):
    if compVariable == "scissors": print("u win comp:", compVariable)
    if compVariable == "paper": print("u lose comp:", compVariable)

def playerVariableCheckScissors(compVariable):
    if compVariable == "paper": print("u win comp:", compVariable)
    if compVariable == "stone": print("u lose comp:", compVariable)

def playerVariableCheckPaper(compVariable):
    if compVariable == "stone": print("u win comp:", compVariable)
    if compVariable == "scissors": print("u lose comp:", compVariable)

def variables():
    rng = random.Random()
    N = 2
    variable = rng.randrange(N)

    return variable

def compVariables():
    compVariable = variables()
    if compVariable == 0: compVariable = "stone"
    if compVariable == 1: compVariable = "scissors"
    if compVariable == 2: compVariable = "paper"
    return compVariable


def startGame():
    playerVariableCheckDraw(playerVariables(), compVariables())


startGame()
print("игра завершена")