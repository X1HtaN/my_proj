#===========task1===========

#def getSquare (a, b):
#    return 0.5*a * b

#print(getSquare(2,4))

#===========task2===========

#def getSquare (a,b):
#    return a * b

#def getPer (a,b):
#    return 2 * (a + b)

#def choice (choice, a, b):
#    if choice == "Per": return getPer(a,b)
#    elif choice == "Square": return getSquare(a,b)
#    else: print("не правильный формат")

#print(choice("Square", 1, 2))

#===========task3===========

#from audioop import reverse


#def getMaxLst (lst):
#    lst.sort()
#    lst.reverse()
#    return lst[0]

#lst = [1, 2, 5, 7, -2, 6]

#print(getMaxLst(lst))

#===========task4===========

def getProduct (lst):
    product = 1
    for i in lst:
        product *= i
    return product

lst = [1,4,6,8,12]

print(getProduct(lst))