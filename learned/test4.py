#=========task1==========

#lst = []

#while True:
#    N = int(input("введите целове число, кроме 0\n"))

#    if (N != 0):
#        lst.append(N ** 2)
#    else:
#        break

#print(lst)

#=========task2==========

#lst = ["+7912123456", "+7915213456", "+6915213456" , "+4915213456", "+7915213456"]
#for i in lst:
#    if lst.count(i) != 1:
#        lst.remove(i)
#    if "+7" in i:
#        lst.remove(i)

#print(lst)

#=========task3==========

#from itertools import count


#lst = [1, 2, 3, 4, 5, 6]
#counter = 0
#x = 0

#while True:
#    counter += 1
#    if counter == 6: break

#    x = lst[0]
#    lst.remove(x)
#    lst.append(x)

#    print(lst)

#=========task4==========

# lst = [1, 2, 3, 4, 5, 6]
# counter = 0
# x = 0

# while True:
#     counter += 1
#     if counter == 6: break
#
#     x = lst[5]
#     lst.remove(x)
#     lst.insert(0, x)
#
#     print(lst)
#
# print()

lst = [x+1 for x in range(6)]
for i in range(len(lst)):
    print(lst)
    lst.pop(0)
    lst.append(i+1)
