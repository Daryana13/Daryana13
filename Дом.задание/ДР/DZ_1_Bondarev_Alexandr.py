import random
r = random.randint(100, 999)
r = str(r)
print("Вывод случайного 3-х значного: ", r)
a = int(r[0])
b = int(r[1])
c = int(r[2])

print("Сумма цифр числа:", a + b + c)
