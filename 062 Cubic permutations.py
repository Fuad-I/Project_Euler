from math import sqrt


def min_solution(num):
    if sqrt(num) == int(sqrt(num)):
        return 0
    y = 10000000
    while True:
        print(y)
        if sqrt(1 + num*y*y) == int(sqrt(1 + num*y*y)):
            return sqrt(1 + num*y*y)
        y += 1


def min_solution2(num):
    x = num + 1
    while True:
        print(x)
        if sqrt((x*x-1)/num) == int(sqrt((x*x-1)/num)):
            return x
        x += 1


'''max_val = 0
for i in range(1, 1000):
    print(i)
    temp = min_solution(i)
    if temp > max_val:
        max_val = temp

print('max_val is', max_val) '''
print(min_solution2(61))
