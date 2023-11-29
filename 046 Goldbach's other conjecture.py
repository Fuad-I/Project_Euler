from functions import is_prime


def check(num):
    for item in primes_list:
        if item > num:
            break
        temp = (num - item)/2
        if pow(int(temp ** 0.5), 2) == pow(temp ** 0.5, 2):
            return True
    return False


primes_list = [x for x in range(1, 10000) if is_prime(x)]
comp_list = [x for x in range(2, 10000) if not is_prime(x) and x % 2 == 1]
print(comp_list)

for item in comp_list:
    if not check(item):
        print('answer is', item)
        break
