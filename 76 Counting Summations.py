def sum_ways(target):
    ways = [1] + [0] * target
    for i in range(1, target):
        for j in range(i, target + 1):
            ways[j] += ways[j - i]
    return ways[target]


print(sum_ways(100))
