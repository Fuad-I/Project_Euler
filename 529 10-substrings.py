
output = 0
for i in range(100, 1000):
    lst = [int(x) for x in str(i)]
    if (sum(lst[0:2]) == 10 and sum(lst[1:3]) == 10) or sum(lst) == 10:
        output += 1
        print(i)
print(output)
