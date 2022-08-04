for i in range(5):
    if i % 2 == 0:
        continue
    print(i)

i = 0
while i < 10:
    i += 1
i -= 10
print(i)

for i in range(1, 10):
    i -= 5
print(i)

'a' + 'x' if '123'.isdigit() else 'y' + 'b'

print(
    '$100 $200 $300'.count('$'),
    '$100 $200 $300'.count('$', 5, 10),
    '$100 $200 $300'.count('$', 5),
)
s = "fghhjkkllhgfdxxxx"
s[::-3]
print(s)
