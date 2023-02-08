#==========task1===========
#n = 6 #1 * 2 * 3 * 4 * 5 * 6 = 720

#def factar(n):
#    res = 1
#    for i in range (1, n+1):
#        res *= i
#    return res

#print(factar(n))

#==========task2===========

#n = [3,4,8,9] #6
#arifm = lambda lst: sum(lst) / len(lst)

#def sum(lst):
#    res = 0
#    for i in lst:
#        res += i
#   return res

#print(arifm(n))

#==========task2===========
lst = [20,2,5,4,5,6,9,8,10,17,11,12,13,7,15,14]

def sort(func, lst):
    return sorted(i for i in lst if func(i))
print(sort(lambda i: True if i % 2 == 0 else False, lst))