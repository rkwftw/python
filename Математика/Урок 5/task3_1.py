import numpy as np
import itertools
import math


k, n = 0, 1000

a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1

k1, n1 = 2, 4

cc = ((math.factorial(n1))/(math.factorial(k1)*math.factorial(n1-k1)))
v = cc*(0.5**k1)*(0.5**(n1-k1))

print(f' проверка С: {cc}')
# print(a, b, c, d)
# print(x)
print(f' успехов:{k}, выборка:{n}, вероятность по Монте-Карло:{k/n}, Биномиальное:{v}')
