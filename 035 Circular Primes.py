from functions import is_prime


def rotations(num):
    nums = [x for x in str(num)]
    for i in range(len(str(num)) - 1):
        nums.append(nums.pop(0))
        temp = int(''.join(nums))
        if not is_prime(temp):
            return False
    return True


lst = [x for x in range(1, 1000000) if is_prime(x)]

result = 0
for item in lst:
    if rotations(item):
        result += 1

print(result)
