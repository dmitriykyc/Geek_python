# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры
# класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker():
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Оклад:': 300000, 'Премия:': 120000}

class Position(Worker):
    def get_full_name(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}'

    def get_total_income(self):
        return f'Доход составляет: {self._income["Оклад:"] + self._income["Премия:"]}'


a = Position('Кусов', 'Дмитрий', 'Генеральный')

print(a.get_full_name())
print(a.get_total_income())

