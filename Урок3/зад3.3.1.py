s = 'Hello world'
print(s[::3])   # распеч.каждый 3 символ
print(s[1] + s[3]) # первый и последний символ
          # обратны порядок


print('..'.join(['a', 'b']))
print('1_2_3'.split('_'))

a = input("введите строку: ")
s = s.split(" ")
print(s)
s = ''.join(s)
print(s)
if s == s[::-1]:
    print("полидром")
else:
    print("не полидром")