# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
#
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.

#Win 10 x64. Python 3.9.6

import sys

# Вариант 1

count = {}
for i in range(2, 99):
    for j in range(2, 10):
        if i % j == 0:
            count[j] = count.get(j, 0) + 1

for k, v in count.items():
    print(f'Чисел кратных числу {k} : {v}')

print(f'Размер объекта count равен: {sys.getsizeof(count)}')
print(f'Размер объекта j равен: {sys.getsizeof(j)}')
print(f'Размер объекта i равен: {sys.getsizeof(i)}')
print(f'Размер объекта v равен: {sys.getsizeof(v)}')
print(f'Размер объекта k равен: {sys.getsizeof(k)}')

# Размер объекта count равен: 360
# Размер объекта j равен: 28
# Размер объекта i равен: 28
# Размер объекта v равен: 28
# Размер объекта k равен: 28

# Вариант 2

num = []
num_2 = [2, 3, 4, 5, 6, 7, 8, 9]
for i in range(2, 100):
    num.append(i)

def multiple(num_x, num_y):
    result = 0
    for idx in num_y:
        for z in num_x:
            if z % idx == 0:
                result += 1
        print(f' Чисел кратных числу {idx} : {result}')
        result = 0

multiple(num, num_2)

print(f'Размер объекта num равен: {sys.getsizeof(num)}')
print(f'Размер объекта num_2 равен: {sys.getsizeof(num_2)}')
print(f'Размер объекта multiple равен: {sys.getsizeof(multiple)}')

# Размер объекта num равен: 920
# Размер объекта num_2 равен: 120
# Размер объекта multiple равен: 136

# Вариант 3

result = {}
for n in range(2, 10):
    result[n] = []
    for f in range(2, 100):
        if f % n == 0:
            result[n].append(f)
    print(
        f'Чисел кратных числу {n} : {len(result[n])}'
    )

print(f'Размер объекта result равен: {sys.getsizeof(result)}')
print(f'Размер объекта n равен: {sys.getsizeof(n)}')

# Размер объекта result равен: 360
# Размер объекта n равен: 28

# Вывод:
# Варианты 1 и 3 наиболее эффективные по использованию памяти