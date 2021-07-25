a = float(input("Введите числитель: "))
b = float(input("Введите знаменатель: "))
def num_func(a, b):
    if b == 0:
        return "На ноль делить нельзя, выберите другой знаменатель"
    else:
        return a / b
print(num_func(a, b))
