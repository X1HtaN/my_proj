class clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        self.seconds = seconds % self.__DAY

    @property
    def get(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.get_format(h)}:{self.get_format(m)}:{self.get_format(s)} "

    @classmethod
    def get_format(cls, x):
        return str(x).rjust(2, "0")

    @classmethod
    def check_format(cls, other):
        if not isinstance(other, (int, __class__)):
            raise ArithmeticError("число не инт")

    #сложение
    def __add__(self, other):
        self.check_format(other)

        sc = other
        if isinstance(other, __class__):
            sc = other.seconds

        return clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.check_format(other)

        return self

    #вычетание
    def __sub__(self, other):
        self.check_format(other)

        sc = other
        if isinstance(other, __class__):
            sc = other.seconds
            if other.seconds > self.seconds:
                return clock(0)
        return clock(self.seconds - sc)

    def __rsub__(self, other):
        return self - other
    
    def __isub__(self, other):
        self.check_format(other)
        return self

    #умножение
    def __mul__(self, other):
        self.check_format(other)

        mul = other
        if isinstance(other, __class__):
            mul = other.seconds
        return clock(self.seconds * mul)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.check_format(other)
        return self

    #деление
    def __truediv__(self, other):
        self.check_format(other)

        truediv = other
        if isinstance(other, __class__):
            truediv = other.seconds

        if truediv < self.seconds / truediv:
            return clock(0)
        return clock(self.seconds / truediv)
    
    def __rtruediv__(self, other):
        return self / other

    def __itruediv__(self, other):
        self.check_format(other)
        return self

    #целочисленное деление
    def __floordiv__(self, other):
        self.check_format(other)

        floordiv = other
        if isinstance(other, __class__):
            floordiv = other.seconds

        return clock(self.seconds // floordiv)
    
    def __rfloordiv__(self, other):
        return self / other

    def __ifloordiv__(self, other):
        self.check_format(other)
        return self

    #процент от деления
    def __mod__(self, other):
        self.check_format(other)

        mod = other
        if isinstance(other, __class__):
            mod = other.seconds

        return clock(self.seconds % mod)
    
    def __rmod__(self, other):
        return self / other

    def __imod__(self, other):
        self.check_format(other)
        return self

c1 = clock(1000)
c2 = clock(2000)
print(c1.get)
c1 = c1 % 10
print(c1.get)
c3 = c1 % c2
print(c3.get)
c4 = 20 % c1
print(c4.get)
c1 %= 20
print(c1.get)