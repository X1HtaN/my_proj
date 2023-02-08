class dataBase:

    __start_values = {
        "name": "None",
        "age": "None",
        "id": "None"
    }

    def __init__(self):
        self.__dict__ = self.__start_values

db1 = dataBase()
db2 = dataBase()

print(db1.name, db1.age, db1.id)
print(db2.name, db2.age, db2.id,"\n")

db1.name = "alex"
db2.age = "25"
db1.id = "1"

print(db1.name, db1.age, db1.id)
print(db2.name, db2.age, db2.id)
