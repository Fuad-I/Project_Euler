from functions import is_prime


def is_trunctable_prime(num):
    if not is_prime(num):
        return False
    div = 10
    while div < num:
        if not (is_prime(num % div) and is_prime(num//div)):
            return False
        div *= 10
    return True


s = 0
count = 0
i = 23

while count < 11:
    if is_trunctable_prime(i):
        count += 1
        s += i
    print(i)
    i += 2

print(s)
