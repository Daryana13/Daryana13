# Есть словарь, где ключ - название продукта. Значение - список , который содержит
# цену и кол-во товара.
# Выведите через "-" название - цену - количество
# С клавиатуры вводится название товара и его количество. n - выход из программы
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке.

product = {'Lays': [5, 10],
           'Estrella': [4, 6],
           'Онега': [3, 5],
           'Pringls': [9, 18]}
for key, value in product.items():
    print(key, '-', value[0], '-', value[1])
price = 0
while True:
    product_1 = input("Выберите товар: ")
    if product_1 == 'n' or product_1 not in product.keys():
        break
    kol = int(input("Выберите количество: "))
    if kol > product[product_1][1]:
        print("Данного количества нет")
        continue
    price += product[product_1][0] * kol
    product[product_1][1] -= kol
print(f"Итого {price} руб.")
print('___________________')
for key, value in product.items():
    print(key, '-', value[0], '-', value[1])


