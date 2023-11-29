from functions import is_prime


def n_th_prime(n):
    count = 2
    i = 5
    while True:
        if is_prime(i):
            count += 1
        if count == 10001:
            return i
        if is_prime(i + 2):
            count += 1
        if count == 10001:
            return i+2
        i += 6


print(n_th_prime(10001))
