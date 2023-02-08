class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        x = self.x
        y = self.y
        return x*x + y*y

    def __bool__(self):
        return self.x == self.y

p = Point(2,3)

print(len(p))

if p:
    print("аргументы одинаковые")
else:
    print("аргументы разные")