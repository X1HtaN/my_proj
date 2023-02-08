#=======task1========
#number = input("введите номер по рпимеру 8(543)4254356\n")

#number = number.replace("(", "").replace(")", "").replace(" ","")

#if (len(number) == 11):
#    print("номер введен верно")
#else:
#    print("номер введен не корректно")

#=======task2========

#string = "2+3+6.7 + 82 + 5.7 +1"

#print(string.replace(" ","").replace("+", "-"))

#=======task3========

#string = "0; -100; 5.6; -3"

#string = string.split("; ")

#for i in string:
#    print(i.rjust(10))

#=======task4========

string = "abrakadabra"

value = string.count("ra")

i = 0

start = 0

while i != value:
    raIndex = string.index("ra", start)

    print(raIndex)

    start = start + raIndex + 1

    i += 1