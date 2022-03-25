#4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

list_abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

letter1 = input("Введите первую букву: ").lower()
letter2 = input("Введите вторую букву: ").lower()

index_letter1 = list_abc.index(letter1) + 1
index_letter2 = list_abc.index(letter2) + 1

if index_letter1 < index_letter2:
    x = 1
else:
    x = -1

print(f'Первая буква {letter1}, находится на позиции: {index_letter1}')
print(f'Вторая буква {letter2}, находится на позиции: {index_letter2}')
print(
    f'Между ними находятся буквы \
{list_abc[list_abc.index(letter1) + x:list_abc.index(letter2):x]} \
({abs(index_letter1 - index_letter2) - 1})'
        )