from math import log

count = 0
for i in range(1, 10):
    count += log(10, 2)//log(10/i, 2)
print(count)
