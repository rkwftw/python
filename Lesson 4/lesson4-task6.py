from itertools import cycle, count

# n = int(input("Введите стартовое целое число: "))
# for i in count(n):
#     print(i)

list1 = [1, True, 2.5, "123"]
for i in cycle(list1):
    print(i)