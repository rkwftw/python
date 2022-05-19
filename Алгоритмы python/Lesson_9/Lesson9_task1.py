# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача
# считается не решённой.

import hashlib

st = input('Введите строку: ')


def substr_counter(s):
    n = len(s)
    hashes = []
    substrs = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            curr = s[i: j]
            if curr == ' ':
                continue
            if curr == st:
                continue
            substrs.append(curr)
            hashes.append(hashlib.sha1(s[i: j].encode('utf-8')).hexdigest())
    print(f'Множество уникальных подстрок: {set(substrs)}')
    print(f'Множество уникальных хэшей подстрок:\n{set(hashes)}')
    return len(set(hashes))


print(f'Количество уникальных подстрок: {substr_counter(st)}')