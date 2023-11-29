"""max_val = 0
target = 0

for i in range(2, 1000, 2):
    count = 0
    for j in range(2, i//3):
        if (i*(i - 2*j)) % (2*(i - j)) == 0:
            count += 1
    if count > max_val:
        max_val = count
        target = i

print(target, max_val) """

from random import randrange
from itertools import permutations
from math import pi, sqrt


def steps(n):
    value = 0
    for i in range(n):
        value += randrange(-1, 2, 2)

    return abs(value)


result = 0
for i in range(1000):
    result += steps(16)

print(result/1000)
print(sqrt(2*16/pi))
