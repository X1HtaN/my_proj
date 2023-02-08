t = '''Куда, ты скачешь гордый конь,
И где опустишь ты копыта?
О мощный властелин судьбы!
Не так ли ты над самой бездной,
На высоте, уздой железной
Россию поднял на дыбы?'''

def replaced(rep):
    replaced = [".",",","\n","!","?"]
    for i in replaced:
        if i == "\n": rep = rep.replace(i, " ")
        else: rep = rep.replace(i, "")
    return rep

def variator(lst):
    for i in range(len(lst)):
        if i%2 == 0:
            print(lst[i], end=" ")
        else: continue

t = replaced(t)
t = sorted(t.lower().split(" "))

variator(t)