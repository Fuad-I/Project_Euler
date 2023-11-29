import math


ans = 0
for i in range(11, 100000):
    if sum([math.factorial(int(x)) for x in str(i)]) == i:
        ans += i

print('answer is', ans)
