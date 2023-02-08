from memory_profiler import memory_usage
import time

start1 = time.time()

def devider(n):
    deviders = [1, n]
    helpDevider = 0
    if n % 2 == 1: return deviders
    else:
        for i in range(2, int(n/2 + 1)):
            if n % i == 0:
                helpDevider = n / i
                deviders += [i]
            else: continue

        return sorted(deviders)

#n = int(input("введите число\n"))
n = int(6540234600)

print(devider(n))

end1 = time.time() - start1

start2 = time.time()

def devider(n):
    deviders = []
    for i in range(1, n+1):
        if n % i == 0: deviders += [i]
        else: continue
    return deviders

#n = int(input("введите число\n"))

print(devider(n))

end2 = time.time() - start2

print(end1, end2)