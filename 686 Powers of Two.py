import math


def compute(n):
    lower = math.log(1.23, 10)
    upper = math.log(1.24, 10)
    cons = math.log(2, 10)
    count = 0
    j = 90
    power = 0
    while count < n:
        print(count, j)
        temp = j*cons
        if upper <= (temp - int(temp)):
            j += 93
        elif lower > (temp - int(temp)):
            j += 196
        else:
            power = j
            j += 196
            count += 1

    return power


print(compute(678910))
