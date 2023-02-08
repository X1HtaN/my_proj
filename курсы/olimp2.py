t = 66 #изначально
r = 83 #дино
l = 57 #стоимость
p1 = 54 #первый товар баллы
p2 = 78 #второй товар баллы
p3 = 98 #третий товар баллы
res = t
cost = r*l
counter = 0

def asd(cost, res):
    if cost > res:
        return True
    else:
        return False

def zxc(res, p):
    res += p
    return res

while cost > res:
    if asd(cost, res):
        res = zxc(res, p1)
        counter += 1
    else: break
    if asd(cost, res):
        res = zxc(res, p2)
        counter += 1
    else: break
    if asd(cost, res):
        res = zxc(res, p3)
        counter += 1
    else: break

print(counter)