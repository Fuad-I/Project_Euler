from math import factorial
from functools import lru_cache
from functions import is_prime


@lru_cache
def s(p):
    return sum([factorial(p-i) for i in range(1, 6)]) % p


result = 0
for i in range(5, 100, 6):
    result += s(i) + s(i+2)
    print(i, s(i))
    print(i+2, s(i+2))

print('found', result)
