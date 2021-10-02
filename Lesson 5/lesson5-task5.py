import random

with open("text5.txt", "w") as file:
    for i in range(20):
        file.write(f'{random.randint(0, 10)} ')

with open("text5.txt") as file:
    x = file.read().split()
    summ = 0
    for j in x:
        summ += int(j)

print(f'Сумма: {summ}')