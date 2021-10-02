def my_func ():
    sum_a = 0
    b = False
    while b == False:
        x = input("Введите строку чисел, разделенных пробелом или Q для завершения: ").split()
        a = 0
        for y in range(len(x)):
            if x[y] == "q" or x[y] == "Q":
                b = True
                break
            else:
                a = a + int(x[y])
        sum_a = sum_a + a
        print(f'Текущая сумма: {sum_a}')
    print(f'Итоговая сумма: {sum_a}')
my_func()