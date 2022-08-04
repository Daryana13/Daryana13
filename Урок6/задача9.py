#Даны два целых числа m и n (m<n) напишите программу которая выводит все числа от m до n включительно
# в порядке возрастания, если m<n или в порядке убывания
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if a > b:
        for i in range(b, a, -1):
            print(i)
            i += 1
    print(i)