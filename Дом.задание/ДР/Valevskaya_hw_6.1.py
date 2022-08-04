# Дан список. Все числа списка проверить на четность.
# Если четное - посчитать сумму его цифр.
# Нечетное - заменить его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.

list = [15, 48, 'hello', 6, 19, 'world']
glas = 0
soglas = 0
for i in list:
    if type(i) == int:
        if i % 2 == 0:
            sum = i % 10 + i // 10
            print(sum)
        else:
            ind = list.index(i)
            list[ind] = 1
    else:
        for j in i:
            if j in 'aeiuo':
                glas += 1
            else:
                soglas += 1
print(list)
print(glas)
print(soglas)