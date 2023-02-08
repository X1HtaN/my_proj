#==========task1==========

#dct = {}

#while True:
#    get = input ("введите числа / end для подсчета \n")

#    if (get == "end"): break

#    get = int(get)

#    dct[get] = get**2

#print(dct)

#==========task2==========

#dct = {}
#i = 0
#string = "int= целое чилсо, dict= словарь, list= список, str= строка, bool= булевый тип"
#string = string.replace("= ", ", ")

#lst = string.split(", ")

#while i != len(lst):
#    dct[lst[i]] = lst[i+1]
#    i += 2

#print(dct)

#==========task2==========

dct = {}
lst = []

while True:
    get = input("введите англ слово / end для вывода словаря\n")
    if get == "end":break

    while True:
        get2 = input("введите переводы / end2 для ввода след. слова \n")
        if get2 == "end2":break

        lst.append(get2)
    
    dct[get] = lst
    lst.clear()

print(dct)