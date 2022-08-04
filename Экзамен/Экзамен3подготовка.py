# # 1.Реализовать калькулятор с 4 методами: Сумма, вычитаниеб, умножение, деление.Метод принимает
# # 2 аргумента и возвращает результат.Невалидные данные должны быть обработаны
#
# class Calculator:
#     def valdate_numbers(self, first_number, second_number):
#         is_valid_first_number = isinstance(first_number, int) or isinstance(first_number, float)
#         is_valid_secon_number = isinstance(second_number, int) or isinstance(second_number, float)
#         if is_valid_first_number and is_valid_secon_number:
#             print("Valid")
#         else:
#             raise Exception("Not Valid")
#     def summ(self, first_number, second_number):
#         self.valdate_numbers(first_number, second_number)
#         summ = first_number + second_number
#         return summ
#     def difference(self, first_number, second_number):
#         self.valdate_numbers(first_number, second_number)
#         diff = first_number - second_number
#         return diff
#     def multiplication(self, first_number, second_number):
#         self.valdate_numbers(first_number, second_number)
#         multip = first_number * second_number
#         return multip
#     def division(self, first_number, second_number):
#         self.valdate_numbers(first_number, second_number)
#         if second_number == 0:
#             print("It cannot be divided by 0")
#         else:
#             div = first_number / second_number
#             print(div)
#             return
#
# my_calc = Calculator()
# my_calc.summ(1, 2)
# my_calc.difference(1, 2)
# my_calc.multiplication(1, 2)
# my_calc. division(1, 0)

#2.Вы идете в путешествие, надо подсчитать сколько у денег у
# каждого студента.Класс студен описан следующим образом:
#Необходимо понять у кого больше всего денег и вернуть его имя.Если у студентов денег поровну вернуть: “all”.
class Student:
    def __init__(self, name, money):
        self.name = name
        self.money = money
student_1 = Student("Petya", 100)
student_2 = Student("Kolya", 110)
student_3 = Student("Nikolai", 1000)

students = [student_1, student_2, student_3]
moneys =[]
for student in students:
    moneys.append(student.money)
print(moneys)
if max(moneys) == min(moneys):
    print('all')
else:max_money = 0
for student in students:
    if student.money > max_money:
        name = student.name
print(max_money)
print(name)



#3.метод sum(a, b) принимает 2 числа и возвращает их сумму.Написать декоратор,
# # который возвращает ошибку если переданы нечисловые параметры(например строка) примерно такое:
#
# # @validate_int_parameters
# # def sum(a,b)
# #     sum(3, "1") => ошибка
# #     sum(4,2) => 6
# def validate_int_parameters(fn):
#     def a_wrapper_accepting_arguments(arg1, arg2):
#         is_valid_a = isinstance(arg1, int) or isinstance(arg1, float)
#         is_valid_b = isinstance(arg2, int) or isinstance(arg2, float)
#         if is_valid_a and is_valid_b:
#             print("ok")
#         else:
#             raise Exception("Not valid")
#         print(fn(arg1, arg2))
#     return a_wrapper_accepting_arguments
#
# @validate_int_parameters
# def sum(a, b):
#     return a + b
# sum(7, 5)
#4.Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы,
# успеваемость(массив из пяти элементов). Создать класс School: Добавить возможно для добавления
# студентов в школу Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки,
# равные только 5 или 6. Добавить возможность вывода учеников заданной группы Добавить возможность
# вывода учеников претендующих на автомат(средний балл >= 7)
#5. Создайте класс Робот создайте 2 типа оружия: меч, автомат Создайте 2 типа амуниции: броня, шлем
# Добавьте оружию и амуниции свои характеристики(например урон, прочность) Создайте своего робота с каким
# либо оружием (может быть несколько и брони может быть несколько.Так же может быть ничего) Выведите весь
# # арсенал робота на экран
#
# class Students:
#
#     def __init__(self, name, group, progress):
#         self.name = name
#         self.group = group
#         self.progress = progress
#
#     def __repr__(self):
#         return self.name
# class School:
#
#     def __init__(self, students):
#         self.students = students
#
#     def get_list_of_students(self):         # получить список студентов
#         return self.students
#
#     def admission(self, student):        # поступление в школу
#         self.students.append(student)
#
#     def remove(self, student, group):    # удаление из школы по группе
#         if student.group == group:
#             self.students.remove(student)
#
#     def print_names(self):                  # написать имена студентов
#         for student in self.students:
#             print(student.name)
#
#     def print_group(self, group):  # вывод учеников одной группы
#         students = []
#         for student in self.students:
#             if student.group == group:
#                 students.append(student)
#         return students
#
#     def get_list_automate_students(self, auto_mark=7):  # студенты с нужным средним баллом
#         list_automate = []
#         for student in self.students:
#             average_grade = sum(student.progress) / len(student.progress)
#             if average_grade >= auto_mark:
#                 list_automate.append(student)
#         return list_automate
#
#     def get_list_of_student_with_needed_mark(self, grades):    # вывод учеников с определенными оценками
#         list_std = self.students.copy()
#         for student in self.students:
#             for mark in student.progress:
#                 if mark not in grades:
#                     list_std.remove(student)
#                     break
#         return list_std

# #6.Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.Даны две различные клетки
# шахматной доски,определите, может ли король попасть с первой клетки на вторую одним ходом.Пример
# Cell 1 coordinates:4, 4 Cell 2 coordinated:5, 5 YES Конь Определите, может ли конь попасть с первойклетки
# на вторую одним ходом. Ладья Определите, может ли ладья попасть с первой клетки на вторую одним ходом.
# Ферзь Определите, может ли ферзь попасть с первой клетки на вторую ходом. Слон определите, может ли слон
# попасть спервой клетки на вторую одним ходом.




# 7.Создать 4 фрукта. Апельсин, яблоко, мандарин, банан У всех фруктов
# есть сорт, список витаминов, цена, имя У апельсина, мандарина, банана есть
# метод очистить У яблока метод порезать У банана есть характеристика: кол - во
# калия Создать 4 объекта фрукта и использовать все доступные
# методы и характеристики При вызове метода очистить, должно писаться
# имя фрукта Например:
# apple =Apple("sort", [a, b, c], 120, "apple")
# apple.clear()
# >>"apple очищен"

