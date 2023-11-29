from functions import sum_of_divisors

print(sum(i for i in range(1, 10000) if not sum_of_divisors(i) == i and sum_of_divisors(sum_of_divisors(i)) == i))
