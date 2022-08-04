# простеший калькулятор
a =float(input('Введите 1 число: '))
b =float(input('Введите 2 число: '))
c = str(input('Дествие: '))
while b >= 0:
    if c == '+':
        print(a + b)
        break
    elif c == '-':
        print(a + b)
        break
    elif c == '*':
        print(a * b)
        break
    elif c == '/':
        if b == 0:
            print('Делить на ноль нельзя, ошибка!')
        else:
            print(a / b)
        break
else:
    print('Делить на ноль нельзя, ошибка!')