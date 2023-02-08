#task2
class Format:
    @classmethod
    def check_format_name(cls, name):
        if not isinstance(name, str): raise ValueError("имя должно быть строкой")

    @classmethod
    def check_format_group(cls, group_number):
        if not isinstance(group_number, str): raise ValueError("номер группы должен быть строкой")

    @classmethod
    def check_format_age(cls, age):
        if not isinstance(age, int): raise ValueError("возраст должен быть числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value): #сеттер
        if self.name == "_name": self.check_format_name(value)
        if self.name == "_age": self.check_format_age(value)
        if self.name == "_group_number": self.check_format_group(value)
        return setattr(instance, self.name, value)

class Student:
    name = Format()
    age = Format()
    group_number = Format()

    def __init__(self, name="Ivan", age=18, group_number="10A"):
        self.name = name
        self.age = age
        self.group_number = group_number

s1 = Student("asd", 14, "12B")
s1._name = "Sergey"
print(f"имя: {s1._name}, возраст: {s1._age}, группа: {s1._group_number}")