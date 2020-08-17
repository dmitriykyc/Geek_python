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
