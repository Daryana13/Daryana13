# # #Задание1
# # class Example:
# #
# #
# #     def __init__(self, num1, num2):
# #         self.num1 = 3
# #         self.num2 = 8
# #     default_hight = 2
# #     default_weidth = 5
# #     def func1(a):
# #         a = int(input("Введите число "))
# #         return a
# #
# #     def func2(self, num1, num2):
# #         return self.num1 + self.num2
# #     def func3(self, hight, weidht):
# #         return self.hight ** self.weidht
# # my_example = Example(2, 4)
# #
# # print(my_example.func1())
# # print(my_example.func2(1, 3))
# # print(my_example.num1)
# # print(my_example.num2)
#
# #Калькулятор
# class Calculator:
#
#     def plus(self):
#         return self.a + self.b
#     def minus(self):
#         return return self.a - self.b
#     def umnoj(self):
#         return self.a * self.b
#     def delen(self):
#         return self.a / self.b
#     try:
#         b == 0
#     except ZeroDivisionError
#         print('На ноль не делится')
# my_calculator = Calculator
# a = int(input('Ведите число: '))
# b = int(input('Ведите число: '))
# oper = input('Введите операцию: ')
# print(my_calculator)

#Задача3
class Human():


    #статические поля
    default_name = "No name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        #динамические поля
        #Публичные
        self.name = name
        self.age = age
        #Приватные
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')
    @staticmethod
    def default_info():
        print(f'Default Name: {Human.default_name}')
        print(f'Default Age: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} money! Current value: {self.__money}')
Human.default_info()                  #вызвать справочника

alexander = Human('Sasha', 27)          #создать объект
alexander.info()                        # вызвать

alexander.earn_money(5000)             #
alexander.earn_money(20000              #
alexander.info()                        #вызов мотод info
