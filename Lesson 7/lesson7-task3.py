class Cell:
    def __init__(self, amount):
        self.amount = int(amount)

    def __str__(self):
        return self.amount * "*"

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if int(self.amount - other.amount) > 0:
            return self.amount - other.amount
        else:
            print("ошибка")


    def __mul__(self, other):
        return Cell(int(self.amount * other.amount))

    def __truediv__(self, other):
        if self.amount // other.amount > 0:
            return Cell(round(self.amount // other.amount))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(self.amount // cells_in_row):
            row += "*" * cells_in_row + "\n"
        row += "*" * (self.amount % cells_in_row) + "\n"
        return row

cell1 = Cell(12)
print(cell1.make_order(5))
cell2 = Cell(15)
print(cell2.make_order(5))
print("сложение: ", cell1 + cell2)
print("вычитание: ", cell2 - cell1)
print("умножение: ", cell2 * cell1)
print("деление: ", cell1 / cell2)

