class Zerodiv:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def divtozero(a, b):
        try:
            return a / b
        except:
            return "Нельзя делить на ноль"

a = int(input("Введите числитель: "))
b = int(input("Введите знаменатель: "))
c = Zerodiv(a, b)
print(c.divtozero(a, b))
