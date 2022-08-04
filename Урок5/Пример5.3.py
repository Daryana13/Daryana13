for i in range(3):         # пример условия else в цикле for
    print(i)
else:
    print('Готово')


i = 0                                 #пример условия else в цикле while
while i < 3:
    print(i)
    i += 1
else:
    print('Готово')

#если применить break с else, то условия не будут выполняться пример:
for i in range(3):
    print(i)
    if i == 1:
        break
else:
    print('Готово')      #выполняется если правильно, и не выполняется если принудительно(break)


