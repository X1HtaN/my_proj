try:
    with open("inner17.1.txt", "r", encoding="utf-8") as file:
        for i in range(100):
            if i % 2 == 0 :
                r = file.read(1)
                with open("outer17.1.txt", "a+", encoding="utf-8") as file2:
                    file2.write(r)
            else:
                file.read(1)
except FileNotFoundError:
    print("файл не найден")

inputStr = str(input("введите текст: "))
inputStr = inputStr.split()
print(inputStr)
try:
    with open("outer17.2.txt", "a+") as file:
        for i in inputStr:
            file.write(i)
            file.write("\n")
except FileNotFoundError:
    print("файл не найден")

import pickle
d = {"house": "дом", "car" : "машина", "tree" : "дерево", "road" : "дорога", "river" : "река"}
d = list(d.items())
try:
    with open("outer17.3.bin", "wb") as file:
        for i in range(len(d)):
            pickle.dump(d[i],file)
    with open("outer17.3.bin", "rb") as file:
        try:
            while i!= "EOFError":
                print(pickle.load(file))
        except EOFError:
            print("скрипт завершен")
except FileNotFoundError:
    print("файл не найден")