# # 1. Найти самое длинное слово в строке
# a = ('cat', 'frog', 'elephant', 'snake', 'parents')
# print(a)
# x = 0
# for i in range(len(a)):
#     if len(a[i]) > len(a[x]):
#         x = i
# print('Самое большое слово - ', a[x])

# 2. Преобразовать текст в список слов
# с удалением знаков препинания

a = input('Введите текст: ')
sin = '''!()-;:?,.'''
for i in a:
    if i in sin:
        b = a.replace(i, '')
print(b)