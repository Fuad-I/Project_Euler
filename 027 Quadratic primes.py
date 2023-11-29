from functions import is_prime

lst = [x for x in range(2, 1000) if is_prime(x)]
d = dict()

for item in lst:
    for j in range(1, item-2, 2):
        if is_prime(1+j+item):
            i = 2
            while True:
                if is_prime(i*i + i*j + item):
                    d[(item, j)] = d.get((item, j), 1) + 1
                    i += 1
                else:
                    break

        if is_prime(1 - j + item):
            i = 2
            while True:
                if i*i - i*j + item < 0:
                    break
                if is_prime(i * i - i * j + item):
                    d[(item, -j)] = d.get((item, -j), 1) + 1
                    i += 1
                else:
                    break

max_val = 0
pair = ()
for k, v in d.items():
    if v > max_val:
        max_val = v
        pair = k
print(pair[0] * pair[1])
