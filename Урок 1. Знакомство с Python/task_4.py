
# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите число: '))
number_text = number
number2 = number % 10
max_number = 0

while number:
    if number2 > max_number:
        max_number = number2
    number //= 10
    number2 = number % 10

print(f'Мы взяли число {number_text} и нашли в нем самую большую цифру, это: {max_number}')