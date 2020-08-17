 #Создать (программно) текстовый файл,
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