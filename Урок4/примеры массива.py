a = [10, 2, 3, 3, 3]
print(a)
b = a.count(3)            #считает сколько 3 в списке
print(b)

a = [10, 2, 3, 3, 3]
print(a)
b = a.index(3)            #позволяет узнать индекс заданного элемента начина с 0 (т.е. номер в списке)
print(b)

a = [10, 2, 3, 3, 3]
print(a)
b = a.pop(3)            #удаляет заданный элемент и выводит список без него
print(b)
print(a)

a = [10, 2, 3, 3, 3]
print(a)
a.remove(3)            #удаляет указанны элемент, т.е. первы найденный соответствующий элемент
print(a)

a = [10, 2, 3, 3, 3]
print(a)
a.reverse()            #переворачивает список, т.е. выводи в обратном порядке
print(a)