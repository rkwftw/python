
def user_func(name, surname, byear, city, email, phone):
    print(f' {name} {surname} {byear} {city} {email} {phone}')
n = input("Введите имя: ")
s = input("Введите Фамилию: ")
b = input("Введите год рождения: ")
c = input("Введите город проживания: ")
e = input("Введите email: ")
p = input("Введите номер телефона: ")
user_func(n, s, b, c, e, p)