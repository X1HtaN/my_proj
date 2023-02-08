import random

string = str(input("введите числа через запятую:\n"))
def funcTry(a):
    print(a)
    try:
        a = int(a)
        return a
    except ValueError as a:
        print("value error", a)
        return "ошибка значения"

newString = map(funcTry, string.replace(",", " ").split())

print(list(newString))

lst = [1,2,3,"4",5]
def arifm(lst):
    out = 0
    try:
        for i in lst:
            i = int(i)
            out += i
        return out / len(lst)
    except ValueError as lst:
        print("value error", lst)
        return "ошибка значения"
    except TypeError as lst:
        print("TypeError", lst) 
print(arifm(lst))

lst = [1,"2a",3,4,5]

def lstDel(lst):
    try:
        delete = random.randrange(1, len(lst)+1)
        check = int(lst[delete-1])
        print(delete)
        yield lst.pop(delete-1)
    except ValueError as lst:
        print("valueErr")
    except TypeError as lst:
        print("typeErr", lst)
    except SyntaxError as lst:
        print("syntaxError")

newLst = lstDel(lst)

print(list(newLst))