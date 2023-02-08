class Math:
    def __init__(self, a, b):
        self.format_check(a)
        self.format_check(b)
        self.a = a
        self.b = b

    @classmethod
    def format_check(cls, item):
        if not isinstance(item, int): raise ValueError("is not int")

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

m1 = Math(4,5)

print(m1.addition())
print(m1.multiplication())
print(m1.division())
print(m1.subtraction())