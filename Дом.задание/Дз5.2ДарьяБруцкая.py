# казино
from random import randint
print('Испытайсвою удачу!')
for i in range(1, 6):
    a = int(input('Введите число от 1 до 10'))
    b = int(input('Выберите цвет: 1 - красный, 2 - чёрный'))
    a_luck = randint(1, 10)
    b_luck = randint(1, 2)
    if a == a_luck and b == b_luck:
        print('Выпало', a_luck, b_luck)
        print('Поздравляем, удача на Вашей стороне!!!')
    else:
        print('Выпало', a_luck, b_luck)
        if i == 5:
            print('Увы, попытки закончились.')
            break
    print('Попробуй ещё раз')
    i += 1
    print()
    print('Попытка', i)