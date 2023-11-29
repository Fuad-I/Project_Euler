def digit_sum(n):
    return sum([int(i) for i in str(n)])


print(digit_sum(pow(2, 1000)))
