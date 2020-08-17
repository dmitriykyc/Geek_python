# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
#
#Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки c помощью инструмента: "{self.title}".')

class Pen(Stationery):
    def draw(self):
        if self.title in ['pan', 'Pan']:
            print('Запуск отрисовки ручкой.')
        else:
            print(f'Вы ввели {self.title}, но рисовать будем тут ручкой.')

class Pencil(Stationery):
    def draw(self):
        if self.title in ['pencil', 'Pencil']:
            print('Запуск отрисовки карандашем.')
        else:
            print(f'Вы ввели {self.title}, но рисовать будем тут карандашем.')

class Handle(Stationery):
    def draw(self):
        if self.title in ['handle', 'Handle']:
            print('Запуск отрисовки маркером.')
        else:
            print(f'Вы ввели {self.title}, но рисовать будем тут маркером.')

s = Stationery('Pan')
s.draw()

p = Pen('Pan')
p.draw()

p = Pen('Фломастер')
p.draw()

pe = Pencil('Pencil')
pe.draw()

h = Handle('handle')
h.draw()
