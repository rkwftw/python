a = input("Введите слова через пробелы: ")
list_a = []
b = 1
for x in range(a.count(" ") + 1):
    list_a = a.split()
    if len(str(list_a)) <= 10:
        print(f" {b} {a[x]}")
        b += 1
    else:
        print(f" {b} {list_a [x] [0:10]}")
        b += 1

