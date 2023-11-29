def fucntion(num):
    temp = num
    while True:
        if sum([int(x)*int(x) for x in str(temp)]) == 1:
            return False
        if sum([int(x)*int(x) for x in str(temp)]) == 89:
            return True
        temp = sum([int(x)*int(x) for x in str(temp)])


count = 0
for i in range(1, 10000000):
    if fucntion(i):
        count += 1
        print(i, fucntion(i))
print(count)
