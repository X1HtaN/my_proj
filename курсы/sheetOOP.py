# class Soda:
#     def __init__(self, ingredient):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None

#     def show_my_drink(self):
#         if self.ingredient:
#             print(f"Газировка и {self.ingredient}")
#         else:
#             print("Обычная гозировка")

# drink1 = Soda(5)
# drink2 = Soda("малина")

# drink1.show_my_drink()
# drink2.show_my_drink()

class TriangleChecker:

    def __init__(self, *args):
        if all(isinstance(arg, int) for arg in args):
            self.args = args
        else:
            self.args = None
        
    def is_triangle(self):
        if self.args != None:
            args = sorted(self.args, reverse=True)
            if args[0] < args[1] + args[2]:
                if all(arg > 0 for arg in self.args):
                    return "Ура! мы сожем сделать треугльник"
                else: return "числа не могут быть отрицательными"
            else: return "жаль, но из этого треугольник не сделать"
        else: return "нужно вводить только числа"