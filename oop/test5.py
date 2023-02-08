class coords:
    min_coord = 0
    max_coord = 200

    @classmethod
    def check(cls, x):
        return cls.min_coord <= x <= cls.max_coord

    @staticmethod
    def square(a,b):
        return a*b

    def __init__(self, x = 0, y = 0):
        if self.check(x) and self.check(y):
            self.x = x
            self.y = y

    def get_coords(self):
        return self.x, self.y

c = coords(2,200)
print(c.get_coords())
print(c.square(2,2))
