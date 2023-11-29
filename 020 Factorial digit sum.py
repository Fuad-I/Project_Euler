from math import factorial


def digit_sum(n):
    return sum([int(i) for i in str(n)])


print(digit_sum(factorial(100)))
