from math import factorial


def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def arrangements(n, k):
    return int(factorial(n) / factorial(n - k))


def permutations(n):
    return int(factorial(n))


# task1
print(f'Задача1: {arrangements(10, 4)}')

# task2
print(f'Задача2: {combinations(4, 1)*combinations(48, 3)+combinations(4, 2)*combinations(48, 2)+combinations(4, 3)*combinations(48, 1)+combinations(4, 4)*combinations(48, 0)}')

# task3
m = 6*2*factorial(5)
n = factorial(7)
print(f'Задача3: P = {m/n}')

# task4
n = combinations(60, 3)
m1 = combinations(50, 3)
m2 = combinations(50, 2)*combinations(10, 1)
print(f'Задача4:\n' 
      f'а) {m1/n}\n'
      f'б) {m2/n}')

# task5
print(f'Задача5: События независимые')

# task6
pab = 99/100
pb = 1/1000
pa = pb*pab+pb*(1-pab)
print(f'Задача6: Вероятность, что действительно болен {(pb*pab)/pa}')