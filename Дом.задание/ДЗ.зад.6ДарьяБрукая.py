# #1/Дан список [15, 48,'hello', 6, 19, 'world'].все числа проверить на чётность.если чётное посчитать его сумму,
# # если не чётное, то заменитьна 1  списке, все слова:посч.кол.гласных и согласных.
# list = [15, 48,'hello', 6, 19, 'world']
# glass = 0
# sogl = 0
# print(list)
# for i in list:
#     if type(i) == int:
#         if i%2 ==0:
#             a = i//10 + i%10
#             print('сумма цифр четного числа',i,'=', a)
#         else:
#             index = list.index(i)
#             list[index] = 1
#     else:
#         for g in i:
#             if g in 'aeyuio':
#                 glass = glass + 1
#             else:
#                 sogl = sogl + 1
# print(list,'Все согласные заменены на 1')
# print(glass,'Гласных букв в списке')
# print(sogl,'Согласных букв в списке')
#Списки(доп)
#1 Дан произвольный список. Представьте его в обратном порядке.
# a = [10, 9, 8, 7, 6, 5, 4]
# a.reverse()
# print(a)

#2 Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует,
# замените его на 200. Обновите список только при первом вхождении числа 20.
# a = [1, 5, 20, 7, 4, 5, 8]
# b = a.index(20)
# a[b] = 200
# print('New a: \n', a)

#3 Список из 7 цифр. Если четных цифр в нем больше чем нечетных, то найти сумму всех его цифр,
# если нечетных больше, то найти произведение 1 3 и 6 элемента.
# a = [1, 2, 3, 4, 5, 6, 7]
# chetn = 0
# nechetn = 0
# b = 0
# c = a[0]
# d = a[2]
# e = a[5]
# for i in a:
#     if i % 2 == 0:
#         chetn = chetn + 1
#     else:
#         nechetn = nechetn + 1
# if chetn > nechetn:
#     for f in a:
#         g = f + b
#     print('Сумма всех цифр в списке', g)
# else:
#     h = c * d * e
#     print('произведение 1, 3, и 6 символа списка: ', h)

#4 Найти совпадающие элементы двух списков.
# a = [5,[1,2],2,'r',4,'ee']
# b = [4,'we','ee',3,[1,2]]
# Эти значения записать в новый список

# a = [5,[1,2],2,'r',4,'ee']
# b = [4,'we','ee',3,[1,2]]
# c = []
# for i in a:
#     for h in b:
#         if i == h:
#             c.append(i)
#             break
# print(c)

#5 Даны 2 списка:
# a = [4,6,'pу','tell',78]
# b = [44,'hello’,56,'exept’,3]
# Выполнить следующие операции:
# 1.Сложить два списка
# 2.Добавьте элемент 6 на 3 позицию.
# 3.Удалите все текстовые переменные
# 4.Посчитайте количество элементов списка
# a = [4,6,'pу',78,'tell']
# b = [44,'hello',56,'exept',3]
# c = a + b
# print(c)
# for i in c:
#     if type(i) is str:
#         c.remove(i)
# print(c)
# s = 0
# for j in c:
#     s += j
# print('Количество элемнтов: ', s)