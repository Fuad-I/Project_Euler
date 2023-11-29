def is_lychrel(number):
    new_num = reverse(number) + number
    for i in range(49):
        if new_num == reverse(new_num):
            return False
        else:
            new_num = reverse(new_num) + new_num
    return True


def reverse(number):
    lst = [x for x in str(number)]
    lst.reverse()
    return int(''.join(lst))


count = 0
for i in range(10000):
    if is_lychrel(i):
        count += 1

print(count)
