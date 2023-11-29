'''from math import factorial as fac


def comb(n, m):
    return fac(n)/fac(m)


total = comb(70, 20)
temp1, temp2 = 18, 18
count = 0

for i in range(2, 8):
    count += (comb(7, i) * (10**i) * comb(temp1, temp2)) / total
    temp1 += 9
    temp2 -= 1

print(count)
print((10**7) / comb(70, 63) * fac(7))'''

