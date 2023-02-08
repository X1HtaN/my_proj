class bd: 
    name = "dodik"
    __age = "22"

    @property
    def old(self):
        return self.__age

    @old.setter
    def old(self, x):
        self.__age = x

    @old.deleter
    def old(self):
        del self.__age

bd1 = bd()

print(bd1.old)
bd1.old = 14
print(bd1.old)
del bd1.old
print(bd1.__dict__)