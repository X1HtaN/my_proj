class learned:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print(f"{self} был удален")

learn = learned(2,5)
print(learn.x, learn.y)
learn.x = 3
print(learn.x)