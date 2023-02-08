a = [[1,2,3],[4,5,6],[7,8,9]]

for i in a:
    for num, j in enumerate(i):
        if j == 1 or j == 5 or j == 8:
            i[num] = 0
print(a)

g = {"house" : "дом", "cat" : "кошка", "car" : "машина"}

def enumerate(sequence, start = 0):
    n = start
    if type(sequence) == dict:
        for elem in sequence.items():
            yield n, elem[0], elem[1]
            n += 1

for i in enumerate(g):
    print(i)

a = [[1,2,3],[4,5,6],[7,8,9]]

def enumerate(sequence, start = 0):
    n = start
    m = 1
    for elem in sequence:
        for j in elem:
            yield n,m,j
            n += 1
        m += 1

for i in enumerate(a):
    print(i)