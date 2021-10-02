def int_func(a):
    b = a[0].upper() + a[1:].lower()
    return b
a = input("Введите слово: ")
print(int_func(a))
c = input("Введите текст: ")
for b in c.split(" "):
    print(f' {int_func(b)} ',end='')