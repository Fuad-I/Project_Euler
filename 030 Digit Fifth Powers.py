def check(num):
    lst = [int(x) for x in str(num)]
    result = 0
    for item in lst:
        result += pow(item, 5)

    return result == num


ans = 0
for i in range(2, 1000000):
    if check(i):
        ans += i

print(ans)
