#  Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
#  Считается, что любые два элемента, равные друг другу образуют одну пару,
#  которую необходимо посчитать.
import random
count = 0
sp = [random.randint(1, 5) for k in range(6)]
print(sp)  # Генерируем список
for i in range(len(sp)):
    for j in range(i + 1, len(sp)):     # От (i + 1) значения цикл
        if sp[i] == sp[j]:          # Считаем кол-во совпадений
            count += 1
print(count)