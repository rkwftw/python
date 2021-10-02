from time import sleep

class Light:
    colors = ("red", "yellow", "green")
    delay = (7, 2, 3)

    def __init__(self):
        self.color = "green"

    def work(self):
        while True:
            for i in self.colors:
                self.__color = i
                print(self.__color)
                sleep(self.delay[self.colors.index(self.__color)])

tlight = Light()
tlight.work()