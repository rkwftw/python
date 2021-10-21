import math

while True:

    sin_deg = int(input("Введите значение в градусах(от 1 до 30): "))
    sin_part = 180/sin_deg

    if 0 < sin_deg <= 30:
        sin_print = math.pi/sin_part
    else:
        print(f'не верное значение')

    print(f'синус {sin_deg} градусов = {sin_print} радиан')
