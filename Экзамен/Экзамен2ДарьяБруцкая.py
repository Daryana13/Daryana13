# 1.	Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt,
# test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os.
import os
print("Test:", os.getcwd())
os.mkdir("Test")
os.chdir("Test")
f_1 = open('test_1.txt', 'w')
f_2 = open('test_2.txt', 'w')
f_3 = open('test_3.txt', 'w')
f_1.close()
f_2.close()
f_3.close()
os.rename('test_1.txt', 'rename_1.txt')
os.rename('test_2.txt', 'rename_2.txt')
os.rename('test_3.txt', 'rename_3.txt')
os.remove('rename_1.txt')
os.remove('rename_2.txt')
os.remove('rename_3.txt')
os.chdir("..")
os.rmdir("Test")


# 2.	Даны два кортежа: C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# Необходимо определить: 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных и максимальных элементов этих кортежей.
# A = (35, 78,21,37, 2,98, 6, 100, 231)
# B = (45, 21,124,76,5,23,91,234)
# sum_A = sum(A)
# sum_B = sum(B)
# if sum_A > sum_B:
#     print("Сумма больше в кортеже - A")
# else:
#     print("Сумма больше в кортеже - B")
# print('min A', min(A), 'Номер - ', A.index(min(A)))
# print('min B', min(B), 'Номер - ', B.index(min(B)))


# 3.	Напишите программу, демонстрирующую работу try\except\finally.
# try:
#     k = 1 / 0
# except ZeroDivisionError:
#     k = 0
# print(k)


# 4.	Создайте 2 множества:
# - Если они одинаковые: вывести что они равны
# - Если 1 множество полностью состоит из второго: вывести сообщение множество 1
# состоит из множества2
# - Если 2 множество полностью состоит из 1: вывести сообщение множество 2
#  	 состоит из множества 1
#
# - Если они пересекаются: вывести элементы в которых они пересекаются
# - Если не пересекаются: вывести сообщение об этом
# import random
# a = [random.randint(1, 100) for i in range(10)]
# b = [random.randint(1, 85) for i in range(10)]
#
# a_set = set(a)
# b_set = set(b)
# print(a_set, b_set, sep = '\n')
#
# if a_set == b_set:
#     print('Одинаковые')
# else:
#     print('Не равны')
#
# if a_set - b_set == set():
#     print('Множество 1 состоит из множества 2')
# if a_set - b_set == set():
#     print('Множество 2 состоит из множества 1')
# if a_set.intersection(b_set):
#     print('Пересекающиеся элементы множеств: ', a_set & b_set)
# else:
#     print('Пересекающихся элементов нет')


# 5.	Создайте словарь из строки ' An apple a day keeps the doctor away'    следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = ['An', 'apple', 'a', 'day', 'keeps', 'the', 'doctor', 'away']
# c = dict(zip(a, b))
# print(c)

# 6.	Ввести 10 чисел, данные числа добавить их во множество.
# import random
# a = [random.randint(0,51) for i in range (10)]
# print(a)
# num_set = set(a)
# print(num_set)
# print(num_set)
# print(months)
# 7.	Найти самое длинное слово в строке.
#
# a = "An apple a day keeps the doctor away"
# a = a.split()
# print(max(a, key=len))


# 8.	Есть словарь песен группы
# Depeche Mode violator songsdict = { 'World in My Eyes': 4.76,
# 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
# Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут
# Создайте новый словарь тех песен, в название которых состоит из одного слова

# songsdict = {'World in My Eyes': 4.76,
#               'Sweetest Perfection': 5.43,
#               'Personal Jesus': 4.56,
#               'Halo': 4.30,
#               'Waiting for the Night': 6.07,
#               'Enjoy the Silence': 4.6,
#               'Policy of Truth': 4.88,
#               'Blue Dress': 4.18,
#               'Clean': 5.68,}
# a = songsdict.values()
# b = songsdict.keys()
# c = 0
# d = []
# e = []
# for i in a:
#     c = c + i
# print("Общее время", c)
# for i in songsdict:
#     if songsdict[i] > 5:
#             d.append(i)
#             print("Список песен, который > 5 минут - ", d)
# for i in b:
#     if ' ' in i:
#         continue
#     e.append(i)
# print("список названий песен из 1 слова", e)



