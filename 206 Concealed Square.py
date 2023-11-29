def match(n):
    s = str(n)
    return all(int(s[i*2]) == i+1 for i in range(9))


num = 138902661  # max possible number
while not match(num*num):
    num -= 2

print(num*10)
