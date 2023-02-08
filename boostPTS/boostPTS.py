import time

count = 0

print("установка трояна")
print("прогресс")
while count < 7:
    time.sleep(1)
    prg_bar = "###" * count
    print(f"\r{prg_bar}", end ="")
    count += 1

print("\n\nтроян установлен\n\n")