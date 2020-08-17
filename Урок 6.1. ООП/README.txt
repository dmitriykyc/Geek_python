# 1. 
# Создать класс TrafficLight (светофор) и определить у него один атрибут
# color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import time
class TrafficLight:
    color = {1: 'Red', 2: 'Yellow', 3: 'Green'}

    def running(self):
        print(self.color[1])
        time.sleep(7)
        print(self.color[2])
        time.sleep(2)
        print(self.color[3])
        time.sleep(7)



go = TrafficLight()
go.running()



# 2. 
# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина ширина масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road():
    def __init__(self, _leight, _width):
        self.leight = _leight
        self.width = _width

    def massa(self):
        return self.leight * self.width * 25 * 5

a = Road(10, 10)
print(a.massa())



# 3. 
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






#  4.
#  Реализуйте базовый класс Car.
#  У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#  Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#  Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
#  и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, derection):
        print(f'Машина {self.name} повернула {derection}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость автомобиля {self.name} составляет: {self.speed}, превышает допустимую 60!')
        else:
            print(f'Скорость автомобиля {self.name} составляет: {self.speed}, всё в порядке, не превышаем')

class SportCar(Car):
    def sport(self):
        if self.speed > 199 and self.color in ['Red', 'Yellow', 'Blue', 'Orange']:
            print(f'Вероятно эта тачка ({self.name}) спортивная')
        else:
            print('Скорее всего это не спорткар... Маленькая скорость, да и цвет не тот...')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость автомобиля {self.name} составляет: {self.speed}, превышает допустимую 40!')
        else:
            print(f'Скорость автомобиля {self.name} составляет: {self.speed}, всё в порядке, не превышаем')

class PoliceCar(Car):
    def police(self):
        if self.is_police == True:
            print('Этот автоомобиль для полиции')
        else:
            print('Это не полицейский автомобиль')

car = Car(70, 'red', 'BMW', None)
car.show_speed()
car.turn('на право')

work_car = WorkCar(75, 'red', 'Audi', None)
work_car.show_speed()

sport = SportCar(270, 'Red', 'BMW', None)
sport.sport()

sport = SportCar(170, 'Red', 'BMW', None)
sport.sport()

police = PoliceCar(170, 'Red', 'BMW', True)
police.police()




# 5.
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



