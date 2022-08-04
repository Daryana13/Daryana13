s = 'Hello everybody'                  # методы
s_2 = 'hello Everybody'
s_3 = 'Hello everybody'
# делаем строку заголовком
print(s.istitle())
#Наин.строку с заглавной
print(s.capitalize())
# переводим строку в нижни регистр
print("\n", s.upper())

# переодим строку  в верхни регистр
print(s.lower())
# Инверси регистра
print(s_2.swapcase())
# проверем, является ли строки заголовками
print(s.istitle())
print(s_2.istitle())
print(s_3.istitle())