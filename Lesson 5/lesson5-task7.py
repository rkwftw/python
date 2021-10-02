import json

comp = {}
count, summ = 0, 0
with open("text7.txt") as file:
    lines = file.readlines()
    for line in lines:
        x = line.split()
        profit = float(x[2]) - float(x[3])
        comp.update({x[0]: profit})
        if profit > 0:
            count += 1
            summ += profit

med_profit = summ / count
res = [comp, {"Средняя прибыль:": med_profit}]
print(res)

with open("t7,json", "w") as file:
    json.dump(res, file)