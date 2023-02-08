class coords:
    def __init__(self, *args):
        self.__coords = args

    def __repr__(self) -> str:
        return f"{self.__coords}"

    def __str__(self) -> str:
        return f"координаты: {self.__coords}"

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return tuple(map(abs, self.__coords))

c = coords(1,2,6,-2)

print(c)
print(len(c))
print(abs(c))