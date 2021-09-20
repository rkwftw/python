import random as rnd
import matplotlib.pyplot as plt

# Да, выглядит фигово, но как научили(никак), так я и накодил

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sum7 = 0
sum8 = 0
sum9 = 0
sum10 = 0

i = 0
for i in range(9):
    x1 = rnd.randint(0, 9)
    x2 = rnd.randint(0, 9)
    x3 = rnd.randint(0, 9)
    x4 = rnd.randint(0, 9)
    x5 = rnd.randint(0, 9)
    x6 = rnd.randint(0, 9)
    x7 = rnd.randint(0, 9)
    x8 = rnd.randint(0, 9)
    x9 = rnd.randint(0, 9)
    x10 = rnd.randint(0, 9)
    list1.append(x1)
    list2.append(x2)
    list3.append(x3)
    list4.append(x4)
    list5.append(x5)
    list6.append(x6)
    list7.append(x7)
    list8.append(x8)
    list9.append(x9)
    list10.append(x10)
    sum1 += x1
    sum2 += x2
    sum3 += x3
    sum4 += x4
    sum5 += x5
    sum6 += x6
    sum7 += x7
    sum8 += x8
    sum9 += x9
    sum10 += x10
    i += 1

list_sum = [sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8, sum9, sum10]

print(
    f'Случайные выборки:\n{list1} \n{list2} \n{list3} \n{list4} \n{list5} \n{list6} \n{list7} \n{list8}'
    f' \n{list9} \n{list10}'
)
print(f'Список сумм: {list_sum}')
plt.hist(list_sum)
plt.show()
