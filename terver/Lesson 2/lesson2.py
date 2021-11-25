import numpy as np
from math import *

# Задача 1
x_values = np.arange(1, 6)
x_probabilities = np.array([0.25, 0.25, 0.25, 0.25, 0.25])

m = x_values.dot(x_probabilities)

y_values = x_values - m
z_values = y_values**2
d = z_values.dot(x_probabilities)

print(f'Задача 1:\n X:{x_values}\n P:{x_probabilities}\n M(x)={m} D(x)={d}')

# Задача 2
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

n = 200
p = 0.01
P = []
# X = combinations(n, k)*(p**k)*(1-p)**(n-k)
for k in range (5, 11):
    P_ = combinations(n, k) * (p ** k) * (1 - p) ** (n - k)
    P.append(P_)

print(f'Задача 2:\n X:{np.arange(5, 11)}\n P:{P}\n Вероятность от 5 до 10 выстрелов={sum(P)} ')

# Задача 3
n = 1421
p = 0.01
P = []
for k in range (0, 10):
    P_ = combinations(n, k) * (p ** k) * (1 - p) ** (n - k)
    P.append(P_)

print(f'Задача 3:\nX:{np.arange(0, 10)}\nP:{P} - вероятность непопадания\np={1-sum(P)} - вероятность попасть к>=10\nn={n} - столько выстрелов нужно')