from math import factorial
from functions import is_prime


def function(num):
    count = 0
    while True:
        if num % 2 == 0:
            count += 1
            num /= 2
        else:
            return count


def comb(num1, num2):
    return factorial(num1) / factorial(num2) / factorial(num1 - num2)


lst = [x for x in range(1000) if is_prime(x)]

