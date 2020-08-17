# 1. 
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, in_str):
        self.in_str = in_str

    @classmethod
    def number(cls, in_str):
        b = [int(i) for i in in_str.split('-')]
        print(f'{b[0]}, {b[1]}, {b[2]}')

    @staticmethod
    def validation(in_str):
        b = [int(i) for i in in_str.split('-')]
        if 0 < b[0] <= 12 and 0 < b[1] <= 31:
            print(f'Все хорошо, дата {in_str}')
        else:
            print('Неверная информация')

# date = Date('120-17-2020')
# date.number('120-17-2020')
Date.validation('12-01-2020')



# 2. 
# Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на нуль.
#
# Проверьте его работу на данных, вводимых пользователем.
#
# При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.

class NoZero(Exception):
    def __init__(self, numb):
        self.numb = numb

a_1 = int(input('Введите делимое: '))
a_2 = int(input('Введите делитель: '))

try:
    if a_2 == 0:
        raise NoZero('Нельзя делить на ноль!')
except ZeroDivisionError:
    print('Нельзя делить на ноль!!!!')
else:
    print(f'Все ок, ваш результат: {a_1/a_2}')


# 3. 
# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
#
#  Проверить работу исключения на реальном примере.
#  Необходимо запрашивать у пользователя данные и заполнять список.
#  Класс-исключение должен контролировать типы данных элементов списка.

# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# # Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.

# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить
# его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести
# текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться

class MyError(Exception):
    def __init__(self, numb):
        self.numb = numb


class Num:
    def comoarison(self, spis):
        a = [i for i in spis if i.isdigit()]
        return a == spis


num = Num()
spis = []
while True:
    num = input('Введите что-то, или введите stop для завершения: ')
    if num not in ['stop', 'Stop']:
        if not num.isdigit():
            print('Вы ввели не число: ')
        else:
            spis.append(num)
    else:
        print(f'Введенный Вами список: {spis}')
        break
try:
    if an.comoarison(spis) == False:
        raise MyError('список состоит не из цифр')
except MyError as er:
    print(er)
else:
    print(f'Все отлично, список {spis} состоит только из цифр')


# 4. 
# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Sklad:
    pass


class Org:
    def __init__(self, color, firm, quantity):
        self.color = color
        self.firm = firm
        self.quantity = quantity


class Print(Org):
    def __init__(self, color, firm, quantity, color_print, speed_print):
        super().__init__(color, firm, quantity)
        self.color_print = color_print
        self.speed_print = speed_print


class Scan(Org):
    def __init__(self, color, firm, quantity, speed_scan):
        super().__init__(color, firm, quantity)
        self.speed_scan = speed_scan


class Xerox(Org):
    def __init__(self, color, firm, quantity, speed_xerox, color_xerox):
        super().__init__(color, firm, quantity)
        self.speed_xerox = speed_xerox
        self.color_xerox = color_xerox


# 5. 
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
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
        self.dict_prod['Кол-во'] = self.quantity
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
        self.dict_prod['Кол-во'] = self.quantity
        self.dict_prod['Скорость сканирования'] = self.speed_scan

        return self.dict_prod


printer = Printer('принтер', 'красный', 'HP', '20', '4+4', '100 стр./мин.')
printer.new_pos()

skan = Scan('Сканер', 'Чёрный', 'HP', '20', '100 стр./мин.')
skan.new_pos()

sklad = Sklad(printer.new_pos(), skan.new_pos())
sklad.quantity()


# 6.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.)

# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
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
        self.dict_prod['Кол-во'] = self.quantity if self.quantity.isdigit() else print(
            'Вы ввели не правильное значение!')
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
        self.dict_prod['Кол-во'] = self.quantity if self.quantity.isdigit() else print(
            'Вы ввели не правильное значение!')
        self.dict_prod['Скорость сканирования'] = self.speed_scan

        return self.dict_prod


printer = Printer('принтер', 'красный', 'HP', '20', '4+4', '100 стр./мин.')
printer.new_pos()

skan = Scan('Сканер', 'Чёрный', 'HP', '20', '100 стр./мин.')
skan.new_pos()

sklad = Sklad(printer.new_pos(), skan.new_pos())
sklad.quantity()




