# def a_function():           #функция
#     print("You just created a function!")
# a_function()          #вызов функции
#
# def empty_function():
#     pass      #пустая операция, когда он выполняется ничего не происходит
#
# #Задача №1 Создать функцию, которая будет считать сумму чисел в списке

# def get_sum():
#     a = 0
#     for i in range(5)
#         a += i
#     print(a)
# get_sum()

# def add(a,b):  #присвоение функции переменной
#     return a+b
# print(add(1,2))  #передача аргументов функции, присвоение функции переменной

# def add(a, b):
#     print(a+b)    #2 принта не может быть, выполнит только 1й второй выводит None
# #    return  a + b
# print(add(a=2, b=3))       #вызов функции по указаному названию аргументов (ключевые аргументы)
# total = add(b=5, a=6)
# print(total)
# def keyword_function(a=1, b=2):  #ключевые аргументы, при создании функнции
#     return a+b
# print(keyword_function(b=4, a=8)) #изменение ключевых аргументов
# print(keyword_function())

# def mixed_function(a, b=2, c=3): #регулярный и ключевой аргумент
#     return a+b+c
# mixed_function(b=4, c=5)   #программа будет выдавать ошибку из-за того что не указали значение регулярного аргумента
# print(mixed_function(1, b=4, c=5))
# print(mixed_function(1))

# def many(*args, **kwargs):     #аргументы (главное звездочки и синтез сразу одна *(кортежи), потом **(словари)
#     print(args) #всегда выводит кортежи
#     print(kwargs)   #всегда выводит словари
# many(1,2,3, name="Mike", job="programmer")

# def function_a():
#     global a        #функция видимости
#     a = 1
#     b = 2
#     return a + b
# def function_b():
#     c = 3
#     return a + c
# print(function_a())
# print(function_b())

#Вложенные функции
# def func1(a,b):
#     def inner_func(x):
#         return x * x * x
#     return inner_func(a) + inner_func(b)
# print(func1(4, 5))

#можно записать в одну строку, если блок простое выражение
def sum(a, b): return a + b