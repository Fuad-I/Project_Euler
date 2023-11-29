from functions import is_prime


list_primes = [x for x in range(2, 10000) if is_prime(x)]


def func(num):
    n = 0
    new_set = set()
    i = 2
    while True:
        if is_prime(num):
            return 1 + len(new_set)
        if num % i == 0:
            num /= i
            new_set.add(i)
        else:
            n += 1
            i = list_primes[n]


k = 645
while True:
    if 4 == func(k) == func(k+1) == func(k+2) == func(k+3):
        print('Found', k)
        break
    k += 1

