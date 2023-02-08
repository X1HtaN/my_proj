#==========task1============

#a = [1,2,-5,0,5,10]
#a = sorted(a)
#for i in range(3):
#    print(a[i], end=" ")

#==========task2============

#digs = (-10, 0, 7, -2, 3, 6, -8)
#print(sorted(digs))

#==========task3============

a = {'+7': 2345678901, '+4': 3456789012, '+5': 5678901234, '+12': 78901234}

def sorter(code):
    code = sorted(code.items(), key=lambda x: int(x[0][1:]))
    return ', '.join([i[0] + str(i[1]) for i in code])


print(sorter(a))