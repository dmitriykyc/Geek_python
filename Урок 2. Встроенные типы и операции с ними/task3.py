#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#Решение через list
number = int(input('Введите месяц в виде целого числа от 1 до 12:'))
months = ['Зима', 'Весна', 'Лето', 'Осень']
if number in [1, 2, 12]:
    print(months[0])
elif number in [3, 4, 5]:
    print(months[1])
elif number in [6, 7, 8]:
    print(months[2])
else:
    print(months[3])

# Второй вариант c dict()

seasons = {'Зима': (1, 2, 12),
       'Весна': (3, 4, 5),
       'Лето': (6, 7, 8),
       'Осень': (9, 10, 11)}

month = int(input('Введите месяц: '))
for i in seasons.keys():
    if month in seasons[i]:
        print(i)

