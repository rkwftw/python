def my_func(a, b, c):
    summ = a + b + c
    return summ - min((a, b, c))
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = my_func(a, b, c)
print(d)