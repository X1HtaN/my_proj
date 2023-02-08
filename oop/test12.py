class half_square:

    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, *args, **kwargs):
        return self.__fn(x) // 2

@half_square
def square(x):
    return x*x

print(square(4))