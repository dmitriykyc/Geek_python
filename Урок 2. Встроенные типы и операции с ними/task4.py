words = input('Введите фразу:')

for i, el in enumerate(words.split(' ')):
    print(i, el[:10]) if len(words) > 10 else print(i, el)

