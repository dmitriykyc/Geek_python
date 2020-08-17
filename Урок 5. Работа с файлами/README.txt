# 1.
# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('task_1.txt', 'a', encoding ='utf8') as text_file:
    while True:
        data = input('Введите данные: ')
        if len(data) != 0:
            text_file.write(data + '\n')
        else:
            print('Вы вышли из программы')
            break

# 2. 
# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text.txt', 'r', encoding='utf8') as text_file:
    data = text_file.readlines()
    print('Количество строк в файле:', len(data))
    for i, nom in enumerate(data):
        print(f'Длина {i + 1} строки: {len(nom.split())} слов.')

# 3.
# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


with open('task_3.txt', 'r', encoding='utf8') as text_file:
    data = text_file.readlines()
    summa = 0
    print('Сотрудники, которые получают менее 20 000 рублей в месяц: ')
    for i in data:
        summa += int(i.split()[2])
        if int(i.split()[2]) < 20000:
            print(i.split()[0])
    print(f'Средняя зарплата по всем сотрудникам: {summa / len(data)} рублей.')

# 4.
# Мне кажется я изобрел слишком сложный велосипед...
with open('task_4.txt', 'r', encoding='utf8') as text_file:
    while True:
        name_number = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        text_f = text_file.readlines()
        a = open('task_4_new.txt', 'a', encoding='utf8')
        for i in text_f:
            if i.split()[0] in name_number:
                a.write(f'{i.replace(i.split()[0], name_number[i.split()[0]])}')
        a.close()
        if not text_f:
            break

# 5. 
# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('task_5.txt', 'r+') as text_file:
    text_file.write('1 2 3 4 5 6 7 8 9')
    sum1 = 0
    text_file.seek(0)
    content = text_file.read()
    for i in content.split():
        sum1 += int(i)
    print(f'Cумма строки {content} = {sum1}')

# 6. 
# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
#
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('task_6.txt', 'r', encoding='utf8') as text_file:
    a = text_file.readlines()
    for str in a:
        new_str = ''.join((i if i in '1234567890' else ' ') for i in str)
        new_2 = [int(i) for i in new_str.split()]
        print(f'{str.split()[0]} {sum(new_2)}')

# 7. 
# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open('task_7.txt', 'r', encoding='utf8') as text_file:
    firmi = {}
    profit = {'average_profit': 0}
    num = 0
    for i in text_file:
        firm = i.split()
        plus = {firm[0]: int(firm[2]) - int(firm[3])}
        firmi.update(plus)
        if int(firm[2]) - int(firm[3]) > 0:
            num += 1
            profit['average_profit'] += (int(firm[2]) - int(firm[3]))
    profit['average_profit'] /= num
    print(firmi, profit)
    with open('task_7.json', 'w') as file_json:
        json.dump(firmi, file_json)
        json.dump(profit, file_json)



