class test1:
    "тестовый класс для изучения"
    width = 400
    height = 300

def perimetr(a,b):
    return (a+b)*2

a = test1() #создание класса а ссылающегося на класс test1
print(test1.__doc__)
print(getattr(a, "width", False))
print(a.__dict__)
print(hasattr(a, "width"))
setattr(a, "circle", 10)
print(a.circle)
delattr(a, "circle")
print(a.__dict__)

w = a.width = 200
h = a.height = 300
print(perimetr(test1.width, test1.height))
print(perimetr(w, h))