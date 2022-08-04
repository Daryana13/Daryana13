import random

i = [1, 3, 'a', 6, 'b']           #через литерал (вражение создающее объект
print(i)

#  данном примере мы создали список с заранее известными данными.Если нужен пусто список, в квадр.скобках ничего не указывается - elemets[]



# через функцию
a = (1, 2, 3)
elements = list(a)
print(elements)

c = [random.randint(0, 100) for i in range(10)]
print(c)

#чтобы добавить новы элемент в список, используем list.append(x), где list - список, x - нужное занчение
element = []
elements.append('a')
elements.append(1)
print(elements)

 # метод list.insert(i, x) ---добавление элементов в список

elements = [1, 3, 'a', 6, 'b']
elements.insert(1, 2)
print(elements)

 #изменение элементов в списке
elements = [1, 3, 'a', 6, 'b']
elements[1] = 2
print(elements)

 #удаление элемента из списка
elements = [1, 3, 'a', 6, 'b']
del elements[1]                        # по индексу удаляет(по порядку
print(elements)

elements = [1, 3, 'a', 6, 'b']     # тоже удаление самого значения
elements.remove('a')
print(elements)

 #Удалять можно как из списка, так и из вложенного
 #
my_list = ['hello', 'world']
elements = [1, 3, my_list, 6, 'a', 'b']
del elements[2][1]   #1 - индекс основного списка 2 - элемент встроенного списка
 # можно удалять целыми диапазонами:

elements = [1, 3, 'a', 'b', 'abc', 123, 435]

del elements[4:]       # удаляем все элементы после 4-го (включительно)
print(elements)

del elements[:2]  # удаляем все элементы до 2-го элемента
print(elements)

del elements[1:3]  # удаляем от 1-го до 3-го элемента
print(elements)

elements = [1, 3, 'a', 'b', 'abc', 123, 435]     # проверить существование элемента в списке
if 'abc' in elements:
    print('Yes.')

a = [1, 3, 5]
b = ["a", 5, 2, 3, 6, 8, 9, 10]
print(a + b)                     # оператором + получаем новый список;
a.extend(b)                     # а при extend в первый список добавляем второй список
print(a)

a = [1, 2, 3, 4]
b = a     #переменно b присваивается не значение списка a, а его адрес
a.append(5)     # оператором равно вы скопируете не список, а его элемент
b.append(6)
print('a', a, 'b', b)

a = [1, 2, 3]
b = a.copy()
print(id(a), id(b), a, b)  # id уникальный номер объекта который храниться в памяти ячейки, при запуске меняется

# для перебора списка используем два метода:
elements = [1, 2, 3, "meow"]      # метод for
for i in elements:
    print(i)

elements = [1, 2, 3, "meow"]     # метод while
elements_len = len(elements)
i = 0
while i < elements_len:
    print(elements[i])
    i += 1


