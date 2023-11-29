new_set = set()
for i in range(2, 101):
    for j in range(2, 101):
        new_set.add(i ** j)

print(len(new_set))
