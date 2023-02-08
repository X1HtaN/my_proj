# def read_last(a):
#     if a <= 0: print("строки не могут быть меньше или равны нулю")
#     try:
#         with open("article.txt", "r", encoding="utf-8") as file:
#             file = file.read().split("\n")
#             text = file[-a:]
#             for i in text:
#                 print(i, end="\n")
#     except FileNotFoundError:
#         print("файл не найден")
# read_last(4)

# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).

def longest_words(file):
    biggest = "1"
    try:
        with open(file, "r", encoding="utf-8") as text:
            text = text.read().replace("\n", " ").split()
            for i in text:
                if len(i) > len(biggest): biggest = i
                else: continue
        print(f"{biggest}, {len(biggest)}")
    except FileNotFoundError:
        print("файл не найден")
longest_words("article.txt")