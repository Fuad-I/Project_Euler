import time
from functools import lru_cache
from functions import is_prime, factorize
import math
import array


@lru_cache
def chain(num):
    if num == 1:
        return 1
    lst = [int(2 ** x) for x in range(1000)]
    if num in lst:
        return lst.index(num) + 1
    return chain(phi(num)) + 1


@lru_cache
def phi(num):
    if is_prime(num):
        return num - 1
    lst = [1] + [x for x in factorize(num)]
    count = num - 1
    for i in range(1, len(lst)):
        count -= num // (lst[i] * lst[i - 1])
    return count


primes_list = list()
with open('2T_part1.txt', 'r') as file:
    for line in file:
        primes_list.extend([int(x) for x in line.split()])
        if primes_list[-1] > 40000000:
            break
while True:
    if primes_list[-1] > 40000000:
        primes_list.pop(-1)
    else:
        break

'''result = 0
i = len(primes_list)
for item in primes_list:
    if phi(item) == 25:
        result += item
    print(i)
    i -= 1 

print(result)'''
start = time.time()
for i in primes_list[:10000]:
    if phi(i) == 25:
        print(i, phi(i))
print(time.time() - start)

