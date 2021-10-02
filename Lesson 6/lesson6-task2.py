class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, volume, depth):
        return self._length * self._width * volume * depth / 1000

res = Road(5000, 20)
print(res.mass(25, 5))