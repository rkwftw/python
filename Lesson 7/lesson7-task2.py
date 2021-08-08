from abc import ABC, abstractmethod

class Textile(ABC):
    @abstractmethod
    def consump(self):
        pass

class Palto(Textile):
    def __init__(self, v):
        self.v = v

    @property
    def consump(self):
        return  f'Расход на пальто: {round(self.v / 6.5 +0.5, 1)}'

class Costume(Textile):
    def __init__(self, h):
        self.h = h

    @property
    def consump(self):
        return f'Расход на костюм: {2 * self.h + 0.3}'

palto = Palto(11)
kostum = Costume(22)

print(palto.consump)
print(kostum.consump)