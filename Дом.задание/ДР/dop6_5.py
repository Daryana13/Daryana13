# 5. Даны два списка.
# 1) сложить два списка
# 2) добавит эл-т 6 на 3 позицию
# 3) удалить все текстовые переменные
# 4) посчитать кол-во эл-в списка

a = [4, 6, 'py', 78, 'tell']
b = [44, 'hello', 56, 'exept', 3]
a.extend(b)
print(a)
a.insert(2, 6)
print(a)
for i in a:
    if type(i) == str:
        a.remove(i)
print(a)
l = len(a)
print('Длина = ', l)