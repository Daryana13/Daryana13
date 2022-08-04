# 4. Найти совпадающие эл-ты двух списков.
# Значения записать в новый список
new = []
a = [5, [1, 2], 2, 'r', 4, 'ee']
b = [4, 'we', 'ee', 3, [1, 2]]
c = a.copy() + b.copy()
print(c)
for i in c:
    if c.count(i) >=2:
        new.append(i)
print(new)

