# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное,
# то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.
My_list = [15, 48, "hello", 6, 19, "world"]
print(My_list)
vowel = 0
consonant = 0
for i in My_list:
    if type(i) == int:
        if i % 2 == 0:
            a = i // 10 + i % 10
            print('сумма цифр четного числа', i, '=', a)
        else:
            index = My_list.index(i)  # находим индекс нечетного числа
            My_list[index] = 1   # заменяем значение этого индеса на 1
    else:
        for j in i:
            if j in 'aoyuie':
                vowel = vowel + 1
            else:
                consonant = consonant + 1
print(My_list, "Все нечетные заменены на 1 в списке")
print(vowel, "Гласных букв в словах")
print(consonant, "Согласных букв в словах")



