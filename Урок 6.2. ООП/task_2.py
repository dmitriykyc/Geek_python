from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param


    @property
    def all_c(self):
        return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'


    @abstractmethod
    def abstract(self):
        return 'Абс метод родитель'


class Coat(Clothes):
    def all_c(self):
        return f'Для пошива пальто потребуется: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Абс метод дочерний'


class Costume(Clothes):
    def all_c(self):
        return f'Для пошива костюма потребуется: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass


coat = Coat(400)
costume = Costume(55)
print(coat.all_c)
print(costume.all_c())
print(coat.abstract())