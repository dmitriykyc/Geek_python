# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

# Не совсем сначала понял задание, вот такой вариант, чтобы пробежать за один забег b км увеличивая на 10% предыдущий.
a1 = int(input('Введите количество км в первый день: '))
b1 = int(input('Введите сколько хотите пробежать: '))
day1 = 0 # Счетчик дней

while a1 < b1:
    a1 *= 1.1
    day1 += 1

print(f'Если бежать на 10% больше чем вчера, вы достигните результата в {a1:.2f} за один забег через {day1} дней.')

# И второй вариант с достижением общего киллометража от всех забегов.

a2 = int(input('Введите количество км: '))
b2 = int(input('Сколько нужно пробежать? '))
day2 = 1 # Считаем дни, 1 - т.к. в переменную km мы уже внесли результат первого дня
km2 = a

while km2 < b2:
    a2 = a2 + (a2 * 0.01)
    km2 += a2
    day2 += 1

print(f'Чтобы пробежать {b2} км. Вам потребуется {day2} дня, точный киллометраж составит: {km2:.2f} км.')
