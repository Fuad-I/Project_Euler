
def sum_ways(target, coins):
    ways = [1] + [0] * target
    for i in range(0, len(coins)):
        for j in range(coins[i], target + 1):
            ways[j] += ways[j - coins[i]]
    return ways[target]


print(sum_ways(200, [1, 2, 5, 10, 20, 50, 100, 200]))
