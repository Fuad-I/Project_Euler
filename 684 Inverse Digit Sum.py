from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    return fibonacci(n-1) + fibonacci(n-2)


def s(n):
    if n < 10:
        return n

    return int(str(n % 9) + n//9 * '9')


def S(n):
    output = 0
    for i in range(1, n+1):
        output += s(i)
    return output


result = 0
for i in range(1, 91):
    print(i, S(fibonacci(i) % 1000000007))


