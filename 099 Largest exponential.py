num_list = list()
with open('p099_base_exp.txt', 'r') as file:
    for line in file:
        num_list.append(tuple(int(x) for x in line.split(',')))

max = (0, 0)
i, j = 0, 0
for item in num_list:
    i += 1
    if item[0] > max[0] ** (max[1] / item[1]):
        max = item
        j = i

print(j)
