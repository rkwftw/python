#2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input("vvedite chislo: ")
even = 0
odd = 0
for i in num:
    j = int(i)
    if j % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'V chisle {num}:\n{even} chetnih cifr\n{odd} nechetnih cifr')