from sys import argv

#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

script_name, virabotka, stavka, premia = argv

print(f'Зарплата сотрудника составит: {(int(virabotka) * int(stavka)) + int(premia)}')