class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_coords(self):
        return f"{self.x} {self.y}"

p = Point(3,4)
print(p.get_coords())