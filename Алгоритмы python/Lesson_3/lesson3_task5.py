# 5. В массиве найти максимальный отрицательный элемент. Вывести на
# экран его значение и позицию в массиве.

import random

rnd = [random.randint(-99, 99) for _ in range(100)]
print(f'Массив: {rnd}')

min_index = 0

for i in rnd:
    if rnd[min_index] > i:
        min_index = rnd.index(i)

if rnd[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент: {rnd[min_index]}.',
            f'Находится в массиве на позиции {min_index}')