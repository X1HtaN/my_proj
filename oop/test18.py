class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    @classmethod
    def check_format(self, item):
        if not isinstance(item, int) or item < 0: raise ValueError("значение не является инт или меньше 0")

    def __getitem__(self, item):
        self.check_format(item)
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("неверный индекс")

    def __setitem__(self, key, value):
        self.check_format(key)
        self.check_format(value)
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None]*off)
        self.marks[key] = value

    def __delitem__(self, key):
        self.check_format(key)
        del self.marks[key]

s1 = Student("сергей", [5,5,2,5,3])
s1[10] = 3
del s1[2]
print(s1.marks)