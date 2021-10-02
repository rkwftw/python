elemnum = int(input("Введите количество элементов списка: "))
list_a = []
x = 0
y = 0
print("Создан список из", elemnum, "элементов. Далее введите значения элементов")
while x < elemnum:
    list_a.append(input("Введите значение для следующего элемента списка: "))
    x += 1
print("Заданный список: ", list_a)
for z in range(int(len(list_a) / 2)):
    list_a[y], list_a[y + 1] = list_a[y + 1], list_a[y]
    y += 2
print("Измененный список: ", list_a)

