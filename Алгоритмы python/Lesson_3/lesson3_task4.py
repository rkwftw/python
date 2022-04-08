# 4. Определить, какое число в массиве встречается чаще всего.

import random

rnd = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {rnd}')

max_index = 0
for i in rnd:
    if rnd.count(max_index) < rnd.count(i):
        max_index = rnd.index(i)

print(f'Число {rnd[max_index]}, встречается {rnd.count(max_index)} раза')