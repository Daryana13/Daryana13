import random
print("Задание 6: Сумма чисел случайного трехзначного числа")
threedigitnumber = random.randint(100, 999)
print("Случайное число:", threedigitnumber)
a = threedigitnumber // 100
b = threedigitnumber % 100
c = b // 10
d = b % 10
print("Результат сложения цифр трехначного числа: ", a+c+d)
