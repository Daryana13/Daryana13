# с помощью while просите пользоател решить пример, пока он не введет правильны ответ.
# Также есть заданное количество попыток.Если он использовал их то вывести сообщение
print("Решите пример 3+4-7=")
a = 0
b = 0
while a == b:
    a += 1
    i = int(input("Ответ:"))
    if i == b:
        print('Правильно')
        break
    else:
        print('Неверно')
