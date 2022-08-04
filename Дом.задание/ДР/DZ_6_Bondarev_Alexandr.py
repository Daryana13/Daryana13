# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.
lst = [15, 48, 'hello', 6, 19, 'world']
a = 0
b = 0
c = 0
for i in lst:
    if type(i) is int:
        if i % 2 == 0:
            i = str(i)
            for n in i:
                n = int(n)
                a += n
            print(i, 'Сумма = ', a)
        else:
            index = lst.index(i)
            lst[index] = 1
    elif type(i) is str:
        for m in i:
            if m in 'aeoiu':
                b += 1
            else:
                c += 1
        print(i, 'Кол-во гласных: ', b)
        print('Кол-во согласных: ', c)
        b = 0
        c = 0
print(lst)