from math import log10, floor

count = 0
num, den = 3, 2
for i in range(1000):
    if floor(log10(num)) > floor(log10(den)):
        count += 1
    temp = den
    den = den + num
    num = den + temp

print(count)
