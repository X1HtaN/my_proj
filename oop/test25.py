class Goods:
    def __init__(self, name, mass, price) -> None:
        super().__init__()
        self.name = name
        self.mass = mass
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.mass}, {self.price}")

class MixinLog:
    ID = 0
    def __init__(self) -> None:
        print("MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id} :товар был продан в 00:00 часов")

    def print_info(self):
        print("info из MixinLog")

class NoteBook(Goods, MixinLog):
    def print_info(self):
        MixinLog.print_info(self)

n = NoteBook("anus", 44, 500)
n.print_info()
n.save_sell_log()