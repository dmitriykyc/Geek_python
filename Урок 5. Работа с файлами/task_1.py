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