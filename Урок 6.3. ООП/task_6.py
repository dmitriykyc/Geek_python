# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.)

#Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

class Sklad:
    def __init__(self, *el):
        self.el = el
        self.a = []

    def quantity(self):
        self.a.append(self.el)
        print(self.a)

class Org:
    def __init__(self, name, color, firm, quantity):
        self.name = name
        self.color = color
        self.firm = firm
        self.quantity = quantity
        self.dict_prod = {}

class Printer(Org):
    def __init__(self, name, color, firm, quantity, color_print, speed_print):
        super().__init__(name, color, firm, quantity)
        self.color_print = color_print
        self.speed_print = speed_print

    def new_pos(self):
        self.dict_prod['Имя'] = self.name
        self.dict_prod['Цвет'] = self.color
        self.dict_prod['Фирма'] = self.firm
        # Проверка
        self.dict_prod['Кол-во'] = self.quantity if self.quantity.isdigit() else print('Вы ввели не правильное значение!')
        self.dict_prod['Сколько цветов'] = self.color_print
        self.dict_prod['Скорость печати'] = self.speed_print

        return self.dict_prod


class Scan(Org):
    def __init__(self, name, color, firm, quantity, speed_scan):
        super().__init__(name, color, firm, quantity)
        self.speed_scan = speed_scan

    def new_pos(self):
        self.dict_prod['Имя'] = self.name
        self.dict_prod['Цвет'] = self.color
        self.dict_prod['Фирма'] = self.firm
        # Проверка
        self.dict_prod['Кол-во'] = self.quantity if self.quantity.isdigit() else print('Вы ввели не правильное значение!')
        self.dict_prod['Скорость сканирования'] = self.speed_scan

        return self.dict_prod


printer = Printer('принтер', 'красный', 'HP', '20', '4+4', '100 стр./мин.')
printer.new_pos()

skan = Scan('Сканер', 'Чёрный', 'HP', '20', '100 стр./мин.')
skan.new_pos()


sklad = Sklad(printer.new_pos(), skan.new_pos())
sklad.quantity()




