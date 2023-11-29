def is_bouncy(number):
    digits = [int(x) for x in str(number)]
    if digits == sorted(digits) or digits == sorted(digits, reverse=True):
        return False
    return True


count_bouncy = 19602
count_not_bouncy = 2178

for i in range(21781, 10000000):
    if is_bouncy(i):
        count_bouncy += 1
    else:
        count_not_bouncy += 1

    if count_bouncy/count_not_bouncy == 99:
        print(i)
        break

print(count_bouncy, count_not_bouncy)
