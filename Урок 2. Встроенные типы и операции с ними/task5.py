my_list = [7, 5, 3, 3, 2]

# number = int(input('Введите число: '))
number = int(input('Введите число: '))
if number > max(my_list):
    my_list.insert(0, number)
elif number in my_list:
    my_list.insert(my_list.index(number), number)
else:
    my_list.append(number)
print(my_list)

# И вот попроще подумал можно сделать:
my_list2 = [7, 5, 3, 3, 2]

number2 = int(input('Введите число: '))
my_list2.append(number2)
print(sorted(my_list2, reverse=True))