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
