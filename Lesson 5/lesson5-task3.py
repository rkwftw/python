with open("text3.txt") as file:
    line1 = file.readlines()
    rab = {}
    summ = 0
    for line in line1:
        zp = line.split()
        rab.update({zp[0]: int(zp[1])})
        summ += int(zp[1])
medzp = summ / len(rab)
print(f'Средняя зп: {medzp}')
for i, j in rab.items():
    if j <= 20000:
        print(f'{i}: {j}')