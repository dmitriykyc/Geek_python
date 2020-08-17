name_stat = []
price_stat = []
qty_stat = []
ed_stat = []
finish = []
i = 1
while i < 4:
    name = input('Введите название: ')
    name_stat.append(name)
    price = input('Введите цену: ')
    price_stat.append(price)
    qty = input('Введите количество: ')
    qty_stat.append(qty)
    ed = input('Введите единицу измерения: ')
    ed_stat.append(ed)
    a = {'Название: ': name, 'Цена: ': price, 'Количество: ': qty, 'Един. изм.: ': ed}
    finish.append((i, a))
    i += 1
print(finish)
print({'Название': name_stat, 'Цена': price_stat, 'Количество': qty_stat, 'Един. изм.': ed_stat})


