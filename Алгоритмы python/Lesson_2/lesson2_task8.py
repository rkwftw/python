# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

range = input("vvedite posledovatelnost bez probelov i zapyatih: ")
num = input("vvedite cifru: ")
count = 0

for i in range:
    if i == num:
        count += 1

print(f'posledovatelnost: {range}\ncifra {num} v nei vstrechaetsa {count} raz')