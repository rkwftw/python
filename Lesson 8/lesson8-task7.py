class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}*i'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a}*i'


z1 = Complex(1, 2)
z2 = Complex(3, 4)
print(f'Сумма z1 + z2 = {z1 + z2}')
print(f'Произведение z1 * z2 = {z1 * z2}')
