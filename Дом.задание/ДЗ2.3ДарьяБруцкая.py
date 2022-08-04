# Принадлежность точки кругу с центром в нач.координат
# c**2=x**2+y**2
# c = sqrt(x**2 + y**2)
print("Введите координаты и радиус")
x = float(input('x: '))
y = float(input('y: '))
r = float(input('r: '))
import math

c = math.sqrt(x**2 + y**2)

if r <= c:
    print('точка принадлежит кругу')
else:
    print('точка не принадлежит кругу')
