# У вас есть словарь, где ключ – название продукта. Значение – список, который содержит цену и кол-во товара.
# Выведите через ‘’–’’ название – цену – количество.
# С клавиатуры вводите название товара и его кол-во. n – выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке.

Product = {'salt': [100, 25],
         'sugar': [200, 50],
         'starch': [300, 30],
         'flour': [400, 40]}
print('__________________________________________________')
print('продукт - цена - количество соответственно')
print('salt', '-',   Product['salt'][0], '-', Product['salt'][1])
print('sugar', '-',  Product['sugar'][0], '-', Product['sugar'][1])
print('starch', '-', Product['starch'][0], '-', Product['starch'][1])
print('flour', '-',  Product['flour'][0], '-', Product['flour'][1])
print('__________________________________________________')
Quantity = 0
price = 0
while True:
    order = input('Выберите товар - ')
    if order == 'n':
        break
    if order not in Product.keys():
        print('Нет в наличии, введите другое\n')
        continue
    if order in Product:
        Quantity = int(input('Введите количество  - '))
    if Quantity > Product[order][1]:
        print('нет в наличии введите меньше\n')
        continue

    price += Product[order][0] * Quantity
    Product[order][1] -= Quantity

    print('\nПродукт добавлен в корзину, для выхода нажмите  "n", \n Если вы желаете приобрести что-нибудь еще: \n')

print('-------------------------------------------------')
print('Оплата - ', price)
print('Остаток - ', Product)
