from functions import get_prime_factors, is_prime


def totient(n):
    result = n
    for num in get_prime_factors(n):
        result = result * (1 - 1/num)
    return result


def n_by_totient(n):
    if is_prime(n):
        return n/(n-1)
    result = 1
    for num in get_prime_factors(n):
        result = result * (1 - 1/num)
    return result


min_value = 1
for i in range(2, 1000000):
    temp = n_by_totient(i)
    if temp < min_value:
        min_value = temp
        print(i)
