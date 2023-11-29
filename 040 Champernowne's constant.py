from math import log

total_len = 0
product = 1
k = 1
for i in range(1, 50000):
    total_len += int(log(i, 10) + 1)
    if total_len >= pow(10, k):
        product *= int(str(i)[int(pow(10, k)) - 1 - total_len])
        k += 1
print(product)
