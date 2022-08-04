# 1. Создайте кортеж с цифрами
# от 0 до 9 и почитайте сумму

# from random import randint
# a = [randint(0,9) for i in range(10)]
# b = tuple(a)
# print('b= ', b, 'Sum = ', sum(b))

# 2. Выведите статистику частности букв в кортеже

# long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и','т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
# print('т =', long_word.count('т'))
# print('а =', long_word.count('а'))
# print('и =', long_word.count('и'))

# 3. Допишите скрипт для расчета средней температуры

week_temp = (26, 29, 34, 32, 28, 26, 23)
sum_temp = sum(week_temp)
days = len(week_temp)
mean_temp = sum_temp / days
print(int(mean_temp))