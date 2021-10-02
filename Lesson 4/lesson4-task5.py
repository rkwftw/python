from functools import reduce

list1 = [x for x in range(100, 1001) if x % 2 ==0]
print(reduce(lambda a, b: a * b, list1))