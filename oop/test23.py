class Geom:
    def get_pr(self):
        raise NotImplementedError("в дочернем классе не определен метод get_pr")

class Square(Geom):
    def __init__(self, a) -> None:
        self.a = a

    def get_pr(self):
        return(self.a * 4)

class Rectangle(Geom):
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def get_pr(self):
        return 2*(self.a + self.b)

class Treangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return(self.a + self.b + self.c)

geom = [Square(3), Square(2),
Rectangle(2,5), Rectangle(6,3),
Treangle(1,2,3), Treangle(4,5,6)]

for i in geom:
    print(i.get_pr())