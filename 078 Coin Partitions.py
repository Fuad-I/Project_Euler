"""def sum_ways(target):
    ways = [1] + [0] * target
    for i in range(1, target):
        for j in range(i, target + 1):
            ways[j] += ways[j - i]
    return ways[target] + 1


'''i = 61
while True:
    if sum_ways(i) % 1000000 == 0:
        print('found', i)
        break
    i += 1
    print(i)'''

lst = [sum_ways(j) for j in range(5,500)]

for i in range(5, 500):
    print(sum_ways(i+1)/sum_ways(i))"""


def smth(n):
    return n or 1


print(smth(0))
