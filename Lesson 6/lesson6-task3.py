class Worker:
    def __init__(self, name, surname, position, income, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._money = {"income": income, "bonus": bonus}

class Position(Worker):

    def get_fullname(self):
        return "{0} {1}".format(self.name, self.surname)

    def get_totalincome(self):
        return self._money["income"] + self._money["bonus"]

worker1 = Position("Vitya", "Pipiskin", "king", 111111, 22222)
print(worker1.name)
print(worker1.surname)
print(worker1._money)
print(worker1.get_fullname)
print(worker1.get_totalincome)
