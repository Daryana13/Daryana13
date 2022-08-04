import random
a = random.randint(100,999)
print('Случаное число=',a)
s = a%10
a = a//10
print('Первый вариант, s =',s, 'a =',a)
s = s+a%10
a = a//10
print('Второй вариант, s =',s, 'a =',a)
s = s+a%10
a = a//10
print('Третий вариант, s =',s, 'a =',a)
print('Сумма цифр числа =',s)