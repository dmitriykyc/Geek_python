# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

vir = int(input('Введите выручку: '))
izd = int(input('Введите издержки: '))
prib = vir - izd

if vir > izd:
    print(f'Прибыль составила: {prib:.2f} рублей')
    sotr = int(input('Введите число сотрудников и я посчитаю прибыль на сотрудника: '))
    prib_sotr =  prib/sotr
    print(f'Прибыль на каждого сотрудника составила: {prib_sotr:.2f} рублей')
elif vir < izd:
    print(f'Убыток составил: {prib:.2f} рублей')
else:
    print('Отработали в 0')
