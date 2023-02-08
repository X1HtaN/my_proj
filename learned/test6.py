#============task1=============

#turp = ("+79123456","+78123456","+77123456","+59123456","+39123456","+76123456")

#for i in turp:
#    if i.count("+7") != 0:
#        print(i)
#    else:
#        continue

#============task2=============

#string = "оценки: 5,4,3,4,2,4,5,4"
#turp = ()

#string = string.replace("оценки: ", "")
#lst = string.split(",")

#for i in range(len(lst)):
#    turp = turp + (int(lst[i]),)

#print(turp)

#============task3=============

turp = ((1,2,3),(4,5,6),(7,8,9))
counter = 1

for i in turp:
    for j in i:
        if (counter % 3 != 0):
            print(j, "-", end = " ")
        else:
            print(j, end = " ")
            print("\n")

        counter += 1