import warnings
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

warnings.filterwarnings('ignore')

# Задача 1
data = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
df = pd.DataFrame(data, columns=["homework"])

mean = sum(data)/len(data)
mean_ = data.mean()

a = []
for x in data:
    a_ = (x - mean)**2
    a.append(a_)
std = np.sqrt(sum(a)/len(a))
std_ = df.std(ddof=0)

m = sum(a)/len(a)
m_ = df.var(ddof=0)
mu = sum(a)/(len(a) - 1)
mu_ = df.var(ddof=1)

print(f'Задача 1:\nmean: {mean} /{mean_}\nstd: {std} /{std_}\nM(смещенная): {m} /{m_}\nM(несмещенная): {mu} /{mu_}')

# Задача 2
q1 = np.quantile(data, 0.25)
q3 = np.quantile(data, 0.75)
iqr = q3-q1
df.boxplot()
boxplot_range = (q1 - 1.5 * iqr, q3 + 1.5 * iqr)

outliers = df[(df <= boxplot_range[0]) | (df >= boxplot_range[1])]
outliers.dropna(inplace=True)

print(f'Задача 2:\n1й квантиль3: {q1}\n3й квантиль: {q3}\nИнтерквартильное расстояние: {iqr}\nВыбросы: {outliers}')
plt.show()

# Задача 3
pb1 = 0.25 #Вероятность учебы на факультете 1
pb2 = 0.25 #Вероятность учебы на факультете 2
pb3 = 0.50 #Вероятность учебы на факультете 3
pab1 = 0.8 #Вероятность сдать сессию на факультете 1
pab2 = 0.7 #Вероятность сдать сессию на факультете 2
pab3 = 0.9 #Вероятность сдать сессию на факультете 3
pa = pab1*pb1+pab2*pb2+pab3*pb3 #Полная вероятность сдать сессию
pb1a = (pb1*pab1)/pa
pb2a = (pb2*pab2)/pa
pb3a = (pb3*pab3)/pa

print(f'Факультет 1: {pb1a}\nФакультет 2: {pb2a}\nФакультет 3: {pb3a}')
