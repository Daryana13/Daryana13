#методы
#clear удаляет все элементы списка
a = [1, 2, 3]
a.clear()
print(a)

#count  Выводит количество элементов повторяющихся(подсчитывает количество заданного элемента)
elements = ["one", "two", "three", "two", "three", "two"]
print(elements.count("one"))

# index - выводит индекс заданного элемента(порядковый номер)
elements = ["one", "two", "three", "two", "three", "two"]
print(elements.index("three"))

# pop - удаляет с индексом (пример 1)
elements = [1, "meow", 3, "meow"]   # pop возвращает удаленный элемент списка
elements.pop(1)
print(elements)

elements.pop()       # удаляем первый элемент
print(elements)

elements.pop(-1)     # удаляем последни элемент
print(elements)

# reverse - переворачивает наш список
a = [1, 2, 3]
a.reverse()
print(a)

# sort сортирует списки по возврастанию
elements = [3, 19, 0, 3, 102, 3, 1]
elements.sort()
print(elements)

# по убыванию
elements = [3, 19, 0, 3, 102, 3, 1]
elements.sort(reverse=True)
print(elements)