class Err(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

if __name__ == "__main__":
    inp = []

    while True:
        a = input("Введите что-нибудь(stop для завершения): ")

        if a == "stop":
            print(f'Финальный список: {inp}')
            break

        try:
            if not a.isdigit():
                raise Err("вы ввели не число")

            inp.append(int(a))
            print(f'Текущий список: {inp}')
        except Err as err:
            print(f'Текущий список: {inp}')
            print(err)

print(inp)
