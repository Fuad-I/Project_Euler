from math import sqrt


def is_pentagonal(num):
    if sqrt(1+24*num) == int(sqrt(1+24*num)):
        return (1 + int(sqrt(1 + 24 * num))) % 6 == 0
    return False


def func():
    lst = [1, 5, 12]
    k = 3
    while True:
        new_num = lst[-1] + k*3 + 1
        k += 1
        for i in range(len(lst) - 1):
            var1 = new_num - lst[i]
            var2 = lst[i]
            if is_pentagonal(var1) and is_pentagonal(abs(var1 - var2)):
                return var1 - var2
        lst.append(new_num)


print(func())
