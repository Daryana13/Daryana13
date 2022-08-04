#Даны два целых числа m и n (m<n) напишите программу которая выводит все числа от m до n включительно
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)
    i += 1