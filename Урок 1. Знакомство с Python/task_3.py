# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number3 = input('Введите число:')
result3_1 = int(number3 ) + int(number3+number3) + int(number3+number3+number3)
print(f'Результат сложения: {number3} + {number3+number3} + {number3+number3+number3} = {result3_1}')
