from string import ascii_letters

class Person:
    __rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    __rus_upper = __rus.upper()

    def __init__(self, fio, old, pas, mass):
        self.verify_fio(fio)

        self.__fio = fio.split()
        self.old = old
        self.pas = pas
        self.mass = mass

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str: raise ValueError("фио должно быть строкой")
        fio = fio.split()
        if len(fio) != 3: raise ValueError("в фио должно быть 3 параметра")

        for i in fio:
            for j in i:
                if not j in ascii_letters + cls.__rus + cls.__rus_upper:
                    raise ValueError("фио должно быть из букв кириллицы")

        for i in fio:
            if len(i) < 1: raise ValueError("фио не может состоять из 1 символа")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old <= 14 or old >= 120: raise ValueError("возраст должен быть числом")

    @classmethod
    def verify_pas(cls, pas):
        if type(pas) != str: raise ValueError("паспорт должен быть строкой")
        pas = pas.split()
        if len(pas[0]) != 4 or len(pas[1]) != 6: raise ValueError("паспорт должен быть в формате | xxxx xxxxxx |")
        for i in pas:
            if not i.isdigit(): raise ValueError("паспорт должен состоять из чисел")

    @classmethod
    def verify_mass(cls, mass):
        if type(mass) != int and type(mass) != float: raise ValueError("вес должен быть целым или вещественным числом")
        if mass <= 20: raise ValueError("вес должен быть больше 20")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def pas(self):
        return self.__pas

    @pas.setter
    def pas(self, pas):
        self.verify_pas(pas)
        self.__pas = pas

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, mass):
        self.verify_mass(mass)
        self.__mass = mass

p = Person("Сергеева Светлана Геннадьевна", 33, "1234 567890", 60)
print(f"{p.fio}, {p.old}, {p.pas}, {p.mass}")

p.old = 45
p.pas = "0987 654321"
p.mass = 21

print(f"{p.fio}, {p.old}, {p.pas}, {p.mass}")