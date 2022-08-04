num1 = float(input('num 1: '))
num2 = float(input('num 2: '))
sign = input('operation (+, -, *, /):')
def sum():
    return num1 + num2
def razn():
    return num1 - num2
def multipl():
    return num1 * num2
def degree():
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'error /0'
if sign == '+':
    print(sum())
elif sign == '-':
    print(razn())
elif sign == '*':
    print(multipl())
else:
    print(degree())
end = input('exit == 0: ')
if end == '0':
    exit()
