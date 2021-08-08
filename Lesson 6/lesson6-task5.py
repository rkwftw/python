class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("start drawing")

class Pen(Stationary):
    def draw(self):
        print("start drawing with pen")

class Pencil(Stationary):
    def draw(self):
        print("start drawing with pencil")

class Marker(Stationary):
    def draw(self):
        print("start drawing with marker")

pen = Pen("a")
pencil = Pencil("b")
marker = Marker("c")
for i in (pen, pencil, marker):
    i.draw