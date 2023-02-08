def opening():
    try: 
        with open("inner19.txt", "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        return("файл не найден")

def translate(a):
    get = {}
    try:
        with open("inner19.txt", "r", encoding="utf-8") as file:
            for i in file:
                i = i.replace("\n", "").replace(":", "").split()
                get.update({i[0] : i[1]})
            for i in get:
                translate = get.get(a)
            return(translate)
    except FileNotFoundError:
        return("файл не найден")

def add(a, b):
    try:
        with open("inner19.txt", "a+", encoding="utf-8") as file:
            file.writelines("\n")
            file.writelines(f"{a} : {b}")
    except FileNotFoundError:
        return("файл не найден")

def delete(a):
    try:
        with open("inner19.txt", "r", encoding="utf-8") as file:
            for i in file:
                i = i.replace("\n", "").replace(":", "").split()
                if i[0] == a:
                    with open("inner19.txt", "r", encoding="utf-8") as newFile:
                        newFile = newFile.read()
                        newFile = newFile.replace(f"\n{i[0]} : {i[1]}", "")
                        with open("inner19.txt", "w", encoding="utf-8") as file:
                            file.write(newFile)
    except FileNotFoundError:
        return("файл не найден")