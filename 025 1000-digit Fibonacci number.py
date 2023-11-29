from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2

    return fibonacci(n-1) + fibonacci(n-2)


i = 1
while True:
    if len(str(fibonacci(i))) == 1000:
        print(i)
        break
    else:
        i += 1
