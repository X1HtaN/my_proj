import math
a = 1
b = 23
t = 1

if t > 2 * 10**9:
    print(0)
else:
    if a > t:
        print(a-t)
    elif b > t:
        print(b-t)
    else:
        while t > min(a,b):
            a += a
            b += b
        print(min(a,b) - t)