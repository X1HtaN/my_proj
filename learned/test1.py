#====les 1====
#word = "abrakadabra"

#count = 0
#i = 0

#while (i < len(word)):
#    if ("a" in word[i]):
#        count += 1
#    i += 1

#print(count)

#====les 2====

#word = "abrakadabra"

#new_word = word[2:7] + word[9:]

#print(new_word)

#====les 3====

#word = str(input())

#count = int(len(word)/2)

#count_plus = count + 1

#if((len(word) % 2) == 0):
#    if (word[0:count] == word[:-count_plus:-1]):
#        print("yes")
#    else:
#        print("no")
#else:
#    if (word[0:count] == word[:-count_plus:-1]):
#        print("yes")
#   else:
#       print("no")

#====les 4====

#word = "abrakadabra"

#count = 0
#i = 0
#j = 0
#while (i < len(word)):
#    j = i + 1
#    if (("r" in word[i]) and ("a" in word[j])):
#        count += 1
#    i += 1

#print(count)

#====les 5====

sentence = input("Введите Ваше предложение: ")

for char in sentence:
    if char != " ": print(char, end="")
    else: print()