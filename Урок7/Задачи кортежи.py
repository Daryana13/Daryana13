# #Созд.кортеж из случ.10 чисел.Найти его махсим.и мин.элемент
# import random
# a = [random.randint(0,100) for i in range (10)]   #от0 до 100 диапазон, (10) количество
# b = tuple(a)
# print(b)
# print('max', max(b), 'min', min(b))

# #
# import random
# a = [random.randint(0, 6) for i in range(10)]
# b = [random.randint(-5, 0) for i in range(10)]
# c = tuple(a + b)
# print(c)
# print(c.count(0))

# #вывести данные кортежа без скобок, через запятую
#
# a = ('hello', 'world')
# a_str = ",".join(a)       #объединяет по запятым
# print(a_str)

# #зд.4. даны два кортежа:
# a = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# b = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# #сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран
# #вывести на экран порядковые номера минималькых элементов этих кортежей
# c = sum(a)
# d = sum(b)
# print(c)
# print(d)
# print('min', min(a), 'min', min(b))
# print(a.index(min(a)))
# print(b.index(min(b)))

# #зад.списки
# #найти совпадающие элементы двух списков, записать в новый список
# a = [5, [1, 2], 2, 'r', 4, 'ee']
# b = [4, 'we', 'ee', 3, [1, 2]]
# print(a + b)

#зад.списки
#два списка:
a = [4, 6, 'py', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]
a.extend(b)
a.insert(3, 6)
print(a)
for i in a:
    if type(i) is str:
        a.remove(i)
a.sort()
print(a)
print(len(a))




