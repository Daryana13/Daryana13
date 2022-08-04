# ДЗ множества
#   Создайте 2 множества:
# - Если они одинаковые: вывести что они равны
# - Если 1 множество полностью состоит из второго: вывести сообщение множество 1
#   состоит из множества2
#
# - Если 2 множество полностью состоит из 1: вывести сообщение множество 2
#   состоит из множества 1
#
# - Если они пересекаются: вывести элементы в которых они пересекаются
# - Если не пересекаются: вывести сообщение об этом
import random
A = set([random.randint(0, 5) for i in range(5)])
print("set A", A)
B = set([random.randint(0, 5) for j in range(5)])
print("set B", B)
print("sets are equal" if A == B else "sets are not equal")
if len(A - B) == 0:
    print('set А consist of set В')
if len(B - A) == 0:
    print('set B consist of set A')
X = A & B
print(f"sets are intersect in {X}" if X else "sets are not intersect")
