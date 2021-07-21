list_a = [7, 5, 3, 3, 2]
print("Текущий рейтинг", list_a)
a = int(input("Введите число: "))
for x in range(len(list_a)):
    if list_a[x] == a:
        list_a.insert(x + 1, a)
        break
    elif list_a[0] < a:
        list_a.insert(0, a)
    elif list_a[-1] > a:
        list_a.append(a)
    elif list_a[x] > a and list_a[x + 1] < a:
        list_a.insert(x + 1, a)
print("Новый рейтинг: ", list_a)
