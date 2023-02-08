import numpy as np
# a = np.array([1, 2, 3, 4])

# b = a.reshape(2, 2)
# print(b[1,1])

a = np.ones((11, 11))
for i in range(len(a)):
    a[5][i] = 0
    a[i][5] = 0
for i in range(len(a)//2):
    a[0][6+i] = 0
    a[10][i] = 0
    a[i][0] = 0
    a[6+i][10] = 0

print(a)