from itertools import permutations
from math import factorial

i = 0
for item in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    i += 1
    if i == 1000000:
        print(''.join(str(x) for x in item))
        break


# Alternatively

lst = list()
target = 0
nums = [int(x) for x in '0123456789']
while True:
    if target == 999999:
        lst.extend(nums)
        break
    for item in nums:
        if target + factorial(len(nums) - 1) < 1000000:
            target += factorial(len(nums) - 1)
        else:
            lst.append(item)
            nums.remove(item)
            break
print(''.join(str(x) for x in lst))
