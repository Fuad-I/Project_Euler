max_sum = 0
for i in range(1, 100):
    for j in range(1, 100):
        if sum([int(x) for x in str(i ** j)]) > max_sum:
            max_sum = sum([int(x) for x in str(i ** j)])

print(max_sum)
