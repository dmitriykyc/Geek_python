# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text.txt', 'r', encoding= 'utf8') as text_file:
    data = text_file.readlines()
    print('Количество строк в файле:', len(data))
    for i, nom in enumerate(data):
        print(f'Длина {i+1} строки: {len(nom.split())} слов.')

