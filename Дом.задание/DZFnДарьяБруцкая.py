#простеши калькул. с введен.двумя числами вещественного типа. ввод с клав.:
# операции +-*/ и два числа.Операции явл.фунц..обработать ошибку:"Деление на ноль"
# Ноль использ.в качестве завершения программы(отдельная операция)

a = int(input("Введите число: "))
b = int(input("Введите число: "))
print('+', '-', '*', '/', '0-exit')
print('oper:')

def sum(a, b):
    return a + b
def razn(a, b):
    return a - b
def umn(a, b):
    return a * b
def delen(a, b):
    if b == 0:
        return "error"
    else:
        return a / b
while True:
    c = input()
    if c == '0':
        break
    else:
        if c == "+":
            print('resul:', sum(a, b))
        if c == "-":
            print('resul:', razn(a, b))
        if c == "*":
            print('resul:', umn(a, b))
        if c == "/":
            print('resul:', delen(a, b))
        print('oper:')
