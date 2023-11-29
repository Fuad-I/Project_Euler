from functions import is_prime

primes_list = [2, 3]
sum_val = 5
i = 5
while True:
    if sum_val + i < 1000000:
        if is_prime(i):
            sum_val += i
            primes_list.append(i)
    else:
        break
    if sum_val + i + 2 < 1000000:
        if is_prime(i+2):
            sum_val += i + 2
            primes_list.append(i+2)
    else:
        break
    i += 6


def function(lst):
    j = 1
    length = len(lst)
    while True:
        for k in range(j+1):
            if is_prime(sum(lst[0+k:length+k])):
                return sum(lst[0+k:length+k]), length-1
        length -= 1
        j += 1


print(function(primes_list))
