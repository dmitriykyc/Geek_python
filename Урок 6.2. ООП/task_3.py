class Cell:
    def __init__(self, quantity):
         self.quantity = quantity

    def __add__(self, other):
        return f'Результат сложения клеток: {self.quantity + other.quantity}'

    def __sub__(self, other):
        return (f'Результат вычетания клеток: {self.quantity - other.quantity}') if \
            (self.quantity - other.quantity) > 0 else 'Клетки больше нет'

    def __mul__(self, other):
        return f'Результат умножения клеток: {self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'Результат деления клеток: {int(self.quantity // other.quantity)}'

    def make_order(self, cl):
        res = ''
        for i in range(1, self.quantity + 1):
            if i % cl != 0:
                res += '*'
            else:
                res += '*\n'
        return res


cell = Cell(100)
cell2 = Cell(17)
print(cell + cell2)
print(cell - cell2)
print(cell * cell2)
print(cell / cell2)
print(cell2.make_order(7))
