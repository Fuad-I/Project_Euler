from math import prod

lst = list()
with open('p008.txt', 'r') as file:
    for line in file:
        lst.extend([int(x) for x in line if x.isnumeric()])

output = 0
for i in range(0, len(lst) - 12):
    if prod(lst[i: i+13]) > output:
        output = prod(lst[i: i+13])
print(output)
