from functions import is_prime


abudant = list()
for i in range(1, 28124):
    if is_prime(i):
        continue
    if sum(x for x in range(1, i) if i % x == 0) > i:
        abudant.append(i)

print(abudant)
new_set = set()
for item in abudant:
    for item2 in abudant:
        if item + item2 < 28124:
            new_set.add(item+item2)

print(sum(set(x for x in range(1, 28124)) - new_set))



