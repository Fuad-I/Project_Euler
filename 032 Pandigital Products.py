numbers = list()
for i in range(9, 100):
    for j in range(100, 1000):
        numbers.append((i, j, i*j))

for i in range(1, 10):
    for j in range(1000, 10000):
        if i * j % 1000 > 0:
            numbers.append((i, j, i*j))

new_set = set()
for lst in numbers:
    if sorted([int(x) for x in str(lst[0]) + str(lst[1]) + str(lst[2])]) == [x for x in range(1, 10)]:
        new_set.add(lst[2])

print(sum(new_set))
