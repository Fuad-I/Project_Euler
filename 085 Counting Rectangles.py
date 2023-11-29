import math

target = 0
grid = [0, 0]
for i in range(1, 100):
    for j in range(1, 100):
        print(i*(i+1)*j*(j+1)//4)
        if math.fabs(2000000 - i*(i+1)*j*(j+1)//4) < math.fabs(2000000 - target):
            target = i*(i+1)*j*(j+1)//4
            grid = [i, j]

print('Taget is', target, grid)
