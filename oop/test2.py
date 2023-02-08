class square:
    def get_square(self,a, b):
        return a*b

a = square()

print(square.get_square(square, 4, 5))
print(a.get_square(2, 3))