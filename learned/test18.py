fio = input("введите фио: ")
fio = fio.split()
print(f"""Ваши персональные данные:
Фамилия: {fio[0]}
Имя: {fio[1]}
Отчество: {fio[2]}""")

try:
    data = []
    with open("inner18.txt","r", encoding="utf-8") as file:
        for i in file:
            i = tuple(i.replace(",", "").split())
            data += [i]
    for i in data:
        if int(i[2]) <= 30:
            print(f"Уважаемы(ая) {i[0]}! Приглашаем Вас принять участие в курсах по изучению Python. Подробную информацию мы выслали на email: {i[1]}")
except FileNotFoundError:
    print("файл не надйен")