eng = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","!"]
rus = ["а","б","с","д","е","ф","г","х","и","ж","к","л","м","н","о","п","ку","р","с","т","ю","в","в","х","й","з"," ","!"]
trans = list(zip(eng, rus))
newStr = str()
str = "hello world!"

def translate(str):
    helpStr = []
    for i in str:
        helpStr.append(rus[eng.index(i)])
    return helpStr

newStrList = list(map(translate, str))

for i in newStrList:
    for j in i:
        newStr += j

print(newStr)
