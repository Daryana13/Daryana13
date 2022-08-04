# #пример рекурсивной функции, когда функция вызывает сама себя
# def factorial(n):
#     if n !=0:
#         return n * factorial(n-1)
#     else:
#         return 1
# print(factorial(5))
#
# def func(x): return x  #присвоение функции переменной, непрямой вызов функции
# a1 = func
# a2 = a1
# print(a2(10))
#
# def sq(x): return x*x
# square=sq               #смена имени функции
#
# #Анонимная функция: лямбда
# product = lambda z,y: x*y     #короткая однострочная функция
# print(product(2,3))
#Функция фнутри функции, можем создавать вызывать и возврыщать из других функций
# def mul(a):
#     def helper(b):  #создаем еще одну внутри mul, она возвращает на функцию helper в каестве результата работы
#         return a*b
#     return helper
# print(mul(3)(2))   #вызов функции

#Декоратор фукции
# def first_test():
#     print("Test function 1")
# def second_test():
#     print("Test function 2")

def simple_decore(fn):
    def wrapper():
        print("Start function")
        fn()
        print("Stop function")
    return wrapper
def first_test():
    print("Test function 1")
def second_test():
    print("Test function 2")
# first_test_wrapped = simple_decore(first_test)             #вариант 1
# second_test_wrapped = simple_decore(second_test)
# first_test_wrapped
# second_test_wrapped

@simple_decore                     #вариант 2
def first_test():
    print("Test function 1")
@simple_decore
def second_test():
    print('sfd')

first_test()
second_test()