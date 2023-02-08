class integer: #класс дескриптор
    @classmethod
    def check_int(cls, coord): #проверка на числовой формат переменной
        if type(coord) != int:
            raise TypeError("value not int")

    def __set_name__(self, owner, name): #присвоение имени переменной
        self.name = "_" + name

    def __get__(self, instance, owner): #геттер
        return getattr(instance, self.name) #instance - экземпляр класса | self.name - имя переменной | owner - класс, от которого был создан экземпляр

    def __set__(self, instance, value): #сеттер
        self.check_int(value)
        return setattr(instance, self.name, value) #instance - экземпляр класса | имени переменной | значения

class test:
    x = integer()
    y = integer()
    z = integer()

    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

t = test(1,2,3)
t.z = 8
print(t.__dict__)