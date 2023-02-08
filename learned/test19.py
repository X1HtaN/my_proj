import test19_1

# s = str(input("2 числа через пробел: ")).split()
# print(f"{test19_1.perimetr(s[0], s[1])} and {test19_1.square(s[0], s[1])}")

# test19_1.opening()
# test19_1.translate("daun")
# test19_1.add("daun", "даун")
#test19_1.delete("daun")


while True:
    varior = str(input("выберите функцию: \n 1 перевод слова \n 2 добавление слова \n 3 удаление слова \n 4 открыть список \n 5 завершение работы\n"))
    if varior == "1":
        wordTrans = str(input("введите слово на английском: "))
        test19_1.translate(wordTrans)
        print("\n")
    if varior == "2":
        wordAdd = str(input("введите слово на англ и через пробел его перевод: "))
        wordAdd = wordAdd.split()
        test19_1.add(wordAdd[0], wordAdd[1])
    if varior == "3":
        wordDel = str(input("введите слово на англ, которое хотите удалить: "))
        test19_1.delete(wordDel)
    if varior == "4":
        print("Список: ")
        test19_1.opening()
    if varior == "5": 
        break

