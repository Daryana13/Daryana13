arr = ['жульен', 'сало', 'редьку']
a = input("Введите блюдо")
for i in arr:
    print(i)
    if i == a:
        print("Я не ем ", i)
    else:
        print("я ем ", a)

