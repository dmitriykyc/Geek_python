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
