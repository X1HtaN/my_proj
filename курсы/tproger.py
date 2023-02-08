from operator import itemgetter
from turtle import update
from unittest import result


def tasks(num):
    task = "task" + str(num)
    print(f"{task:-^20}")

tasks(1)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i <= 5: print(i)

tasks(2)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in a:
    for j in b:
        if i == j: c += [j]
print(c)

tasks(3)

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sorted(d))
print(sorted(d, reverse=True))

tasks(4)

dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}
result = {}

for i in (dict_a, dict_b, dict_c):
    result.update(i)

print(result)

tasks(5)

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
my_dict = dict(sorted(my_dict.items(), key=itemgetter(1)))
result = {}
i = 1
for key, value in my_dict.items():
    if i <= 3:
        print(key, ":", value)
    else: continue
    i += 1

tasks(6)

print(int('ABC', 16))

tasks(7)

print("none")

tasks(8)

countForTask8 = 0

def counter(word, countForTask8):
    countForTask8 += 1
    a = len(word)//2
    if countForTask8 == a:
        print("это полиндром")
    return countForTask8

word = "анна"

for i in range(len(word)//2):
    if word[i] == word[-i-1]:
        countForTask8 = counter(word, countForTask8)
        continue
    elif i == 0:
        if word[0] == word[-1]:
            countForTask8 = counter(word, countForTask8)
            continue
    else: 
        print("слово не полиндром")
        break