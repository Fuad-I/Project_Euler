from itertools import permutations
from functools import reduce
from functions import is_prime

for item in permutations(range(7, 0, -1)):
    temp = reduce(lambda num1, num2: 10 * num1 + num2, item)
    if is_prime(temp):
        print(temp)
        break
