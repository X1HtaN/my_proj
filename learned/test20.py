import time
import math
# lst = []
# N = 400000

# def testTime(func):
#     def wrapper(*args):
#         st = time.time()
#         func(*args)
#         dt = time.time() - st
#         print(f"время работы - {dt}")
#     return wrapper

# @testTime
# def app(lst, N):
#     for i in range(0, N+1, 2):
#         lst.append(i)
#     return lst

# @testTime
# def comp(lst, N):
#     lst = [i for i in range(0,N+1,2)]
#     return lst

# app(lst, N)
# comp(lst, N)


x = 16

def cash(func):
    def wrapper(x):
        st = time.time()
        sqrt = func(x)
        print(sqrt)
        dt = time.time()-st
        print(dt)
    return wrapper

@cash
def sqrtX(x):
    return math.sqrt(x)

sqrtX(x)
sqrtX(x)
