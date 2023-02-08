class clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise ArithmeticError("не инт")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __check_format(cls, other):
        if not isinstance(other, (int, __class__)):
            raise TypeError("не класс и не инт")

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__check_format(other)
        return self.seconds == sc
    
    def __lt__(self, other):
        sc = self.__check_format(other)
        return self.seconds < sc
    
    def __le__(self, other):
        sc = self.__check_format(other)
        return self.seconds <= sc

c1 = clock(1000)
c2 = clock(2000)

print(c1 == c2)
print(c1 != c2)
print(c1 < c2)
print(c1 > c2)
print(c1 <= c2)
print(c1 >= c2)