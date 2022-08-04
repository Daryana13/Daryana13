i = 0
while i < 10:                     # способ вырваться из цикла, нужно использовать функцию break
    print(i)
    if i == 5:
        break
    i += 1

i = 1                      # необх.вычислить сумму чисел от 1 до 50 и результат вывести на экран
result = 0
while i <= 50:
    result += i
    i += 1
print(result)

