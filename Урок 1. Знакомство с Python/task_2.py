# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в
# формате чч:мм:сс. Используйте форматирование строк.
time = int(input('Введите число в секундах, я переведу в часы:'))

sec = str(time % 60).zfill(2)
min = str(time // 60 % 60).zfill(2)
hours = str(time // 60 // 60).zfill(2)

print(f'{time} секунд переведем в часы и минуты, получается {hours}:{min}:{sec}')
