from functions import is_prime
from math import pow, log, prod


def div_by_every_num(n):
    primes = [i for i in range(1, n+1) if is_prime(i)]
    return prod(pow(i, int(log(n, i))) for i in primes)


print(int(div_by_every_num(20)))
