# 3. В массиве случайных целых чисел поменять местами минимальный и
# максимальный элементы.

import random

rnd = [random.randint(0, 99) for _ in range(10)]
print(f'Массив до изменения: {rnd}')

max = rnd[0]
min = rnd[0]

for i in rnd:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = rnd.index(min)
max_index = rnd.index(max)
rnd[min_index], rnd[max_index] = rnd[max_index], rnd[min_index]
print(f'Массив после изменения элементов {min_index} и {max_index}: {rnd}')