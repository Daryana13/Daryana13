# dict - словари
# #способ создания через литерал
#
# a = {}
# a = {'dict': 1, 'dictionary': 2}
# print(a)
# # создать через dict словарь и имеет своеобразный синтексис
# a = dict(short = 'dict', long = 'dictionary')
# a_2 = dict([(1, 1), (2, 4)])
# print(a, '\n', a_2)
#
# # fromkeys  создает словарь с ключами и у всех одинаковое значение, или ключи без значений
# d = dict.fromkeys(['a', 'b'])
# d_2 = dict.fromkeys(['a', 'b'], 100)
# # print(d, '\n', d_2)
#
# # с помощью генераторов словарей
# d = {a: a ** 2 for a in range(7)}
# print(d)

# если знаем ключ, то доступ к значению по этому ключу можно получить при помощи операции[].Этим способом можно изменить значение, добавить
# для вывода нового ключа, указываем ключ, а не его индекс
# d = {1: 2, 2: 4, 3: 9}
# d[4] = 4 ** 2
# print(d[1])
# print(d)
# # методы словарей
# # dict.clear() очищает словарь
#
# d = {1: 2, 2: 4, 3: 9, 5: {1: 2, 2: 2, 3: 3, 4: 4}}
# print(d[1])
# print(d)
#
# a = d.copy()           # копирует
# print(a)
#
# print(d.items())       #выводит ключи и значение
#
# print(d.keys())        #выводит только ключи
#
# print(d.pop(1))         #выводит то что удалет, в скобочках указываем ключ, а не индекс
#
# print(d.values())     # выводит только значение
#
# print(len(d))         # определяет длину и выводит количество ключей
#
# c = 2 in d           # операция in, если в ключе значение 2, выводит true false
# print(c)

# #операция del  предназн.для удаления элемента на основе заданного
# d = {1: 2, 2: 4, 3: 9, 5: {1: 2, 2: 2, 3: 3, 4: 4}}
# print(d)
# del d

# position = {'Manager': {'Director',
#                         'Deputy Director'},
#             'Teacher': {'Specialist',
#                         'Methodist',
#                         'Senior Lecturer'},
#             'Staff': {'Cleaner',
#                       'Porter',
#                       'Watchman'}}
# count1 = len(position)
# count2 = len(position['Manager'])
# count3 = len(position['Staff'])
# print(position, 'len:', count1, '\n',
#       position['Manager'], 'len:', count2, '\n',
#       position['Staff'], 'len:', count3, '\n')
# определяем есть ли в словаре  ключ
# удалить элемент поключу
# a = {'DDirector': 120000.0,
#      'Secretary': 101000.25,
#      'Locksmith': 100000.00}
# print(a)
# key = 'Secretary'
# if key in a:
#     del a['Secretary']
#     print(a)
#
# #попытка удалить несуществующее
# key2 = 5
# if key2 in a:
#     del a[key2]
# Операция not in - определение отстствия ключа в словаре
# Создаем пусто словарь
# Words = dict()
# count = int(input("Количество слов в словаре"))
# i = 0
# while
# функция zip позволяет создать словари путем объединения списков ключей и значений
# a = dict(zip([1, 2, 3], ['One', 'Two', 'Three']))
# print(a)
# обход словаря с помощью цикла for и вывод всех пар
Months = {1: 'Jan', 2: 'Feb', 3: 'Mar',
          4: 'Apr', 5: 'May', 6: 'Jun',
          7: 'Jul', 8: 'Aug', 9: 'Sep',
          10: 'Oct', 11: 'Nov', 12: 'Dec'}
for mn in Months:
    print(mn, ':', Months[mn])