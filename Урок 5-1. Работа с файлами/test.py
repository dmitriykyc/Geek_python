with open('task_7.txt', 'r', encoding='utf8') as text_file:
    for i in text_file:
        a = i.split()[4]
        print(i, type(i), a)