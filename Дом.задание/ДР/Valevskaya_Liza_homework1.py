from random import randint
random_number = randint(100, 999)
print(random_number)
import math
r1 = int(random_number//100)
print(r1)
r2 = int(random_number%100//10)
print(r2)
r3 = int(random_number%10)
print(r3)
num = [r1, r2, r3]
print(math.fsum(num))