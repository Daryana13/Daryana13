# Задача 1. Даны действительные числа x и y. Получить x - y  1+xy
x = int(input("x ="))
y = int(input("y ="))
if x > y:
    z = x - y
else:
    z = y - x + 1
print(z)