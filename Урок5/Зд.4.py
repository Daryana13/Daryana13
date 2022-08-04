# вводим два числа с клавиатуры, необх. вывести на экран все отриц.числа, леж.между ними.
a = int(input("Введите числа:  "))
c = int(input("Введите числа:  "))
while a < c:
    print(a)
    a = a + 1
    if a > -1:
        break
while c < a:
        print(c)
        c = c + 1
        if c > -1:
            break
    
