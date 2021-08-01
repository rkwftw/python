list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list2 = [list1[i] for i in range(1, len(list1)) if list1[i - 1] < list1[i]]
print(list2)