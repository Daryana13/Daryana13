# 3. Список из 7 цифр.
# Если четных больше чем нечетных - найти сумму цифр,
# если нечетных больше - найти произведение 1-3-6 эл-в
list = [15, 6, -98, 47, 100, 3, 300]
m = 0
n = 0
sum = 0
for i in list:
    if i % 2 == 0:
        m += 1
        sum += i
    else:
        n += 1
print('Четных =', m)
print('Нечетных =', n)
if m < n:
    pr = list[0] * list[2] * list[5]
    print('Произведение нечетных = ', pr)
else:
    print('Сумма четных = ', sum)