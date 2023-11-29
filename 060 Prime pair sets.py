from functions import is_prime

'''lst = list()
with open('2T_part1.txt', 'r') as file:
    for line in file:
        lst.extend([int(x) for x in line.split()])
print("done")'''


def merge(num1, num2):
    temp = num2
    while temp > 0:
        num1 *= 10
        temp //= 10
    return num1 + num2


numbers = dict()
'''for item in lst[:1230]:
    numbers.update({item: []})
print('done')'''

for item in lst[:1230]:
    for i in range(1230):
        if is_prime(merge(item, lst[i])) and is_prime(merge(lst[i], item)) in lst:
            numbers[item].append(lst[i])

print(numbers)
