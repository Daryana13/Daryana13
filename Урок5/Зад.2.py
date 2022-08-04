# перемножить все чётные значения  в диап от 0 до 125
i = 1
result = 1
while i <= 125:
    if i % 2 == 0:
        result = result * i
    i += 1
print(result)
