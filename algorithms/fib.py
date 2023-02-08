# def fib(n):
#     lst = [0,1]
#     for i in range(2,n+1):
#         lst.append(lst[i-2]+lst[i-1])
#     return lst[-1]

# print(fib(3))

def fib_mod(n, m):
    lst = [0,1]
    f = 0
    s = 1
    for i in range(n):
        f = f + s
        s = f - s
    return f % m

print(fib_mod(1598753,25897))