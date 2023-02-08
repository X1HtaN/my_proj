class Country:
    def __init__(self) -> None:
        self.population = 0

    @classmethod
    def check_format(self, item):
        if not isinstance(item, int): ValueError("население не int")

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, item):
        self.check_format(item)
        self.__population = item

Russia = Country()
Canada = Country()
Germany = Country()

Russia.population = 143400000
Canada.population = 38250000
Germany.population = 83130000

print(Russia.population, Canada.population, Germany.population)