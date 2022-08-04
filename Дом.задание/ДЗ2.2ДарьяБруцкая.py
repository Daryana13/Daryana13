a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and c + b > a:
    print("треугольник существует")
else:
    print("треугольник не существует")
if (c**2 == a**2 + b**2) or (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2):
    print("прямоугольны")
elif (c**2 < a**2 + b**2) or (a**2 < b**2 + c**2) or (b**2 < a**2 + c**2):
    print("острый")
else:
    print("тупоугольный")