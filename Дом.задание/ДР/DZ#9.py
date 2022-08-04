# Есть словарь, где ключ - название продукта. Значение - список , который содержит
# цену и кол-во товара.
# Выведите через "-" название - цену - количество
# С клавиатуры вводится название товара и его количество. n - выход из программы
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке.

product = {'Каштан': [2.10, 10],  # Название - цена - кол-во
           'Столичное': [2.05, 10],
           'Топ': [1.54, 10],
           'Вавёрочка': [1.65, 10]}
total_price = 0  # Цена после первого выбора
full_price = 0   # Итоговая цена
total_amount = 0
print('Есть в наличии следующие варианты: ')
print('Варианты выводятся: "Название" - "Цена" - "Количество"')
print('Каштан',product['Каштан'][0], product['Каштан'][1], sep = '-')
print('Столичное',product['Столичное'][0], product['Столичное'][1], sep = '-')
print('Топ',product['Топ'][0], product['Топ'][1], sep = '-')
print('Вавёрочка',product['Вавёрочка'][0], product['Вавёрочка'][1], sep = '-')
name = ''
count = 0
# stop_word = 'n'
while  product['Каштан'][1] >= 0 and product['Топ'][1] >= 0 and\
        product['Столичное'][1] >= 0 and product['Вавёрочка'][1] >= 0:
    name = input('Введите название мороженого: ')
    count = int(input('Введите количество мороженого: '))
    if name in product:
        for j in product:
            if j == name:
                total_amount = product[j][1] - count   # Оставшееся кол-во
                total_price = count * product[j][0]   # Цена за выбранное в первый раз
                product[j][1] -= count
                full_price += total_price  # Финальная цена за все
                print(f'С вас за все {full_price} бел. руб.')
                print('Остаток',product)
                if product['Каштан'][1] < 0 or product['Топ'][1] < 0 or product['Столичное'][1] < 0 or\
                    product['Вавёрочка'][1] < 0:
                    print('Ошибка, столько нет ')
                    break
    elif name == 'n':
        break
    else:
        print('Повторите название')










