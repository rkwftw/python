list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res = [x for x in list1 if list1.count(x) == 1]
print(res)