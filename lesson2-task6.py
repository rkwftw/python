list_k  = []
n = 1
title, price, amount, units = None, None, None, None
while True:
    if title is None:
        title = input("Введите наименование товара: ")
    if price is None:
        price = input("Введите цену товара: ")
    if amount is None:
        amount = input("Введите количество единиц товара: ")
    if units is None:
        units = input("Введите обозначение единиц товара: ")
    list_k.append((
        n,
        {
            "наименование": title,
            "цена": price,
            "количество": amount,
            "единицы": units
        }
    ))
    title, price, amount, units = None, None, None, None
    n += 1
    print(list_k)
    Q = input("Хотите завести еще одну карточку товара?(y/n): ")
    if Q.lower() == "n":
        break
dict_a = {
    'наименование': [],
    'цена': [],
    'количество': [],
    'единицы': set()
}
for x, item in list_k:
    dict_a['наименование'].append(item['наименование'])
    dict_a['цена'].append(item['цена'])
    dict_a['количество'].append(item['количество'])
    dict_a['единицы'].add(item['единицы'])
print(dict_a)