# #зад.1
import random

n = int(input())
m = int(input())
a = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(1, 100)
        print(a[i][j], end= ' ')
    print()

# #Зад.2
# m = [[1, 3, 4, 9],
#      [-5, 8, 9, 0],
#      [-6, 7, 11, 19]]
# print(m)
# num = int(input("Введите число "))
# for i in range(3):
#     for j in range(4):
#         if m[i][j] == num:
#             print(f"строка {[i+j]}, колонка{[j+i]}")
# else:
#     print("Числа нет в матрице")
#зад.3 исключения
a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
try:
    c = a / b
except ZeroDivisionError:
    print("На ноль делить нельзя")
finally:
    print(c ** 2)

