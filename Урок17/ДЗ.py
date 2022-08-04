#Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
# которая должна быть произведена над ними. Если третий аргумент +, сложить их;
# если —, то вычесть; * — умножить; / — разделить (первое на второе).
# В остальных случаях вернуть строку "Неизвестная операция".
import b as b


def arithmetic():
arg_1 = float(input('Введите первое число: '))
arg_2 = float(input('Введите второе число: '))
operation = input('Введите операцию: ')

if operation == '+':
    print(arg_1 + arg_2)
elif operation == '-':
    print(arg_1 - arg_2)
elif operation == '*':
    print(arg_1 * arg_2)
elif operation == '/':
    print(arg_1 / arg_2)

else:
    print('Неизвестная операция!')

arithmetic()

def arithmetic(a, b, s):
    if s == '+':
return a + b
    if s == '-':
return a - b
if s == '*':
return a * b
if s == '/' and b != 0:
return a / b
return 'Неизвестная операция'

first = float(input('Ввудите первое число:'))
second = float(input('Ввудите второе число:'))
oper = input('Введите оператор:')
print(arithmetic(first, second, oper))

def arithmetic():
try:
num = int(input('Введите первое число:'))
num1 = int(input('Введите второе число:'))
action = input('Выберите действие:(+, -, *, /)')
if action == '+':
    print(num + num1)
elif action == '-':
    print(num - num1)
elif action == '*':
    print(num * num1)
elif action == '/':
    print(num / num1)
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except ValueError:
    print('Неизвестная операция!')

arithmetic()

# обозначаем функцию
def arithmetics(num1, operation, num2):
return_value = "0"
if operation == "+":
return_value = str(int(num1) + int(num2))
elif operation == "-":
return_value = str(int(num1) - int(num2))
elif operation == "*":
return_value = str(int(num1) * int(num2))
elif operation == "/":
if num2 != 0:
return_value = str(int(num1) / int(num2))
else:
return_value = "E-R-R-O-R: cannot divide by zero"
return return_value


# принимаем данные
a = int(input("a = "))
b = int(input("b = "))
operation_with_ab = str(input("operation: "))


# выводим результат
print(str(a), operation_with_ab, str(b), "=", arithmetics(a, operation_with_ab, b))