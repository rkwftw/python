class Warehouse:
    def __init__(self, name):
        self.name = name
        self.wh = []

    def __str__(self):
        return "\n".join(map(lambda x: f'---{str(x)}---', self.wh))

    def put(self, item):
        self.wh.append(item)

    def whtransfer(self, wh_transfer, item_index):
        wh_transfer.put(self.wh[item_index])
        self.wh.remove(self.wh[item_index])


class OfficeStuff:
    def __init__(self, status):
        self.status = status


class Printer(OfficeStuff):
    """Type_ = bw/color, name = производитель, model = модель"""

    def __init__(self, type_, name, model, status="Рабочий"):
        super().__init__(status)
        self.type_ = type_
        self.name = name
        self.model = model

    def __str__(self):
        return f'Принтер тип: {self.type_}, производитель: {self.name}, модель: {self.model}'


class Scanner(OfficeStuff):
    """Type_ = drum/flat/hand, name = производитель, model = модель"""

    def __init__(self, type_, name, model, status="Рабочий"):
        super().__init__(status)
        self.type_ = type_
        self.name = name
        self.model = model

    def __str__(self):
        return f'Сканер тип: {self.type_}, производитель: {self.name}, модель: {self.model}'


class Copier(OfficeStuff):
    """Type_ = analog/digital, name = производитель, model = модель"""

    def __init__(self, type_, name, model, status="Рабочий"):
        super().__init__(status)
        self.type_ = type_
        self.name = name
        self.model = model

    def __str__(self):
        return f'Копир тип: {self.type_}, производитель: {self.name}, модель: {self.model}'


wh1 = Warehouse("Склад")
wh2 = Warehouse("Помойка")
while True:

    a = input("Введите команду('put' для добавления на склад, 'transfer' для переноса, \'"
              "check' для проверки содержимого склада, 'q' для завершения работы): ").capitalize()

    if a == "Put":
        item_type = input("Введите тип устройства (priner/scanner/copier): ").capitalize()

        if item_type == "Printer":
            put_item_type = input("Введите тип (b/w or color): ")
            put_item_name = input("Введите производителя: ")
            put_item_model = input("Введите модель: ")
            item = Printer(put_item_type, put_item_name, put_item_model)
            wh1.put(item)
            print(f'На склад добавлен {item}')

        elif item_type == "Scanner":
            put_item_type = input("Введите тип (drum/flat/hand): ")
            put_item_name = input("Введите производителя: ")
            put_item_model = input("Введите модель: ")
            item = Scanner(put_item_type, put_item_name, put_item_model)
            wh1.put(item)
            print(f'На склад добавлен {item}')

        elif item_type == "Copier":
            put_item_type = input("Введите тип (analog/digital): ")
            put_item_name = input("Введите производителя: ")
            put_item_model = input("Введите модель: ")
            item = Copier(put_item_type, put_item_name, put_item_model)
            wh1.put(item)
            print(f'На склад добавлен {item}')

    if a == "Transfer":
        index_str = input("Введите порядковый номер предмета для переноса: ")
        if index_str.isdigit():
            index_int = int(index_str)
            index_int -= 1
            wh1.whtransfer(wh2, index_int)
        else:
            print(f'Введены не цифры')

    if a == "Check":
        print(f'{wh1.name}:\n{str(wh1)}')
        print(f'{wh2.name}:\n{str(wh2)}')

    if a == "Q":
        print(f'Работа завершена')
        break

    # else:
    #     print(f'Неправильно введена команда')
