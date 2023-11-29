from math import prod
from functions import is_prime


def factorize(num):
    lst = [i for i in range(num) if is_prime(i)]
    output = list()
    j, temp = 0, num
    while temp > 1 and j < len(lst):
        if temp % lst[j] == 0:
            output.append(lst[j])
            temp /= lst[j]
        else:
            j += 1

    return output


def num_of_factors(num):
    return prod([v+1 for v in factorize(num)])


def triangle_number(n):
    return n*(n+1)//2


def solution(n):
    i = 10
    while True:
        if num_of_factors(i) + num_of_factors(i+1) > n:
            return triangle_number(i*(i+1)//2)
        i += 1


print(solution(500))
