def pandigital(num):
    temp = ['0']
    for j in range(1, 4):
        for digit in str(num * j):
            if digit in temp:
                return []
            temp.append(digit)
    return temp


def pandigital2(num):
    temp = ['0']
    for j in range(1, 3):
        for digit in str(num * j):
            if digit in temp:
                return []
            temp.append(digit)
    return temp


max_val = [i for i in '0918273645']

for i in range(900, 988):
    temp_var = pandigital(i)
    if temp_var > max_val:
        max_val = temp_var

for i in range(9000, 9877):
    temp_var = pandigital2(i)
    if temp_var > max_val:
        max_val = temp_var

print(max_val)
