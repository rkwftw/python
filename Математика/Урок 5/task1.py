import random as rnd

while True:
    value = rnd.randint(1, 37)
    a = input(f'press enter to spin')
    if value == 37:
        value = 0
    print(f'result: {value}')
