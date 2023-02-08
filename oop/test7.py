class coords:
    min_coords = 0
    max_coords = 200

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 999

    def __setattr__(self, key, value):
        if type(value) == str:
            raise AttributeError("недопустимый тип атрибута")
        else: object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        if item == "z":
            raise ValueError("недопустимый атрибут")
        else: return object.__getattribute__(self, item)

    def __getattr__(self, item):
        return False #если нету такого атрибута в классе возвращает False

    def __delattr__(self, item):
        print(f"вы удалили объект, {item} в подклассе {self}")


c1 = coords(4,5)
c2 = coords(10,15)

print(f"{c1.x},{c1.y}")
print(f"{c2.x},{c2.y}")

del c1.x