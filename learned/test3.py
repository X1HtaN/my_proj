#=========task1==========

#lst = [-1, 0, 5, 3, 2]

#for i in range(len(lst)):
#    float(lst[i])
#    lst[i] += 7.2
#    print(lst[i])

#print(lst)

#=========task2==========

#lst = []

#while True:
#    N = input("введите числа (для составления списка введите go / для завершения цикла введите end)\n")
#    if (N == "end"): break

#    if (N != "end" and N != "go"): lst += [N] + [N]

#    if (N == "go"):
#        print(lst)

#=========task3==========

#A = [1, 2, 3, 4, 5, 6]
#B = [1, 0, 0, 1, 1, 1]
#C = []

#for i in range(len(A)):
#    C += [A[i] + B[i]]
#    print(C[i])

#print(C)

#=========task3==========

lst = []

while True:
    N = input("введите числа (для составления списка введите go / для завершения цикла введите end)\n")
    if (N == "end"): break

    if (N != "end" and N != "go"): lst += [N]

    if (N == "go"):
        if ("5" in lst): print("есть число 5", lst)
        else: print("числа 5 нету в списке", lst)
        