class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("go")

    def stop(self):
        print("stop")

    def turn(self, direction):
        print(f"Car turns to {direction}")

    def show_speed(self):
        print(f"speed is {self.speed}")

class Towncar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("speed limit violation")

class Sportcar(Car):
    pass

class Workcar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("speed limit violation")

class Policecar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

town = Towncar(111, "red", "town")
sport = Sportcar(222, "green", "sport")
work = Workcar(333, "blue", "work")
police = Policecar(444, "yellow", "police")

town.show_speed()
work.show_speed()
