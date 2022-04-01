#4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

n = int(input("vvedite kolichestvo elementov: "))
i = 0
range = 1
sum = 0
while i < n:
    sum += range
    range /= -2
    i += 1

print(f'summa elementov: {sum}')