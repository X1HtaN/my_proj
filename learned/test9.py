#==========task1============
#a = 28
#b = 35

#def getNOD(a, b):
#    if not b: return a
#    else:
#        if a<b: a,b = b,a 
#        return getNOD(b, a%b)
#print(getNOD(a, b))

#==========task2============

#args = [1, 2, 5, 7, 3 , 10, 6, 15, 22, 3, 5, 43, 11, 42]

#def maxArgs(arg, arg2, i):
#    if(i == len(args)):
#        return arg2
#    elif arg[i] > arg2:
#        arg2 = arg[i]
#        return maxArgs(args, arg2, i+1)
#    else:
#        return maxArgs(args, arg2, i+1)

#print(maxArgs(args, 0, 0))

#==========task3============

args = [2, 5, 7, 3 , 1, 10, 6, 15, 22, 3, 5, 43, 11, 42]
bool = lambda choice: True if choice == "max" else False

def maxArgs(arg, arg2, i):
    if i == len(args):
        return arg2
    elif arg[i] >= arg2:
        arg2 = arg[i]
        return maxArgs(args, arg2, i+1)
    else:
        return maxArgs(args, arg2, i+1)

def minArgs(arg, arg2, i):
    if i == len(args):
        return arg2
    elif arg[i] <= arg2:
        arg2 = arg[i]
        return minArgs(args, arg2, i+1)
    else:
        return minArgs(args, arg2, i+1)

def choiceArgs(args, choice):
    if bool(choice):
        return maxArgs(args, 0, 0)
    else:
        return minArgs(args, args[0], 0)    


print(choiceArgs(args, "min"))