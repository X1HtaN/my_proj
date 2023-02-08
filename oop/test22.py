class Geom:
    def __init__(self,x1,x2,y1,y2) -> None:
        print(f"инициальизация для {self.__class__.__name__}")
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class Line(Geom):
    def __init__(self, x1, x2, y1, y2) -> None:
        super().__init__(x1, x2, y1, y2)

class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None) -> None:
        super().__init__(x1, x2, y1, y2)
        self.fill = fill

l = Line(1,2,3,4)
r = Rect(1,3,5,7,9)
print(l.__dict__)
print(r.__dict__)