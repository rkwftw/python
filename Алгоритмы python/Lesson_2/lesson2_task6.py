# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за
# 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, вывести ответ.

import random


turn = 0
x = random.randrange(100)

while turn < 10:
    print(f'popitka {turn + 1}')
    num = int(input("vvedite chislo ot 0 do 100: "))
    if num == x:
        print("molodec, ugadal")
        break
    elif num < x:
        print(f'ne ugadal, {num} menshe zagadannogo')
    else:
        print(f'ne ugadal, {num} bolshe zagadannogo')
    turn += 1

print("popitki zakonchilis")

