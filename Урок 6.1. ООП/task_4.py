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
