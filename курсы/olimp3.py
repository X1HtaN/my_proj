n = 10 #окр
k = 3 #прыжок
n2 = n
res = 0
counter = 0

while res != n:
    if n < res:
        n * 2
    if n2 % k and n > k:
        res += k + 1
        n2 -= 1
        counter += 1
        print(res)
    else:
        res += k
        print(res)
        counter +=1

print(counter)