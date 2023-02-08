class coords:
    __min_coords = 0
    __max_coords = 200

    @classmethod
    def __check(cls, x):
        return cls.__min_coords <= x <= cls.__max_coords

    def __init__(self, x, y):
        if self.__check(x) and self.__check(y):
            self.__x = x
            self.__y = y
        else:
            print("не верное значение")

    def get_coords(self):
        return self.__x, self.__y

c = coords(1,200)
print(c.get_coords())