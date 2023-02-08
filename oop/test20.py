class Geom:
    name = "Geom"

    def set_coords(self, x, x2, y, y2):
        self.x = x
        self.x2 = x2
        self.y = y
        self.y2 = y2

    def draw(self):
        print("рисование примитива")

class Line(Geom):
    name = "Line"

    def draw(self):
        print("Line")

class Rect(Geom):
    name = "Rect"

l = Line()
r = Rect()
print(l.name, r.name)
l.draw()
r.draw()