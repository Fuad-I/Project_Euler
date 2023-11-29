import math


def factorial_digit_sum(number):
    return sum([math.factorial(int(x)) for x in str(number)])


def chain_len(number):
    count = 1
    lst = [number]
    while True:
        if not factorial_digit_sum(number) in lst:
            count += 1
            lst.append(factorial_digit_sum(number))
            number = lst[-1]
        else:
            break
    return count


total = 0
for i in range(21, 1000000):
    if chain_len(i) == 60:
        total += 1
    print(i, chain_len(i))

print(total)
