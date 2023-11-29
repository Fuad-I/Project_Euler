num1, num2, temp = 1, 1, 0
result = 0

while temp < 4000000:
    temp = num1 + num2
    if temp % 2 == 0:
        result += temp
    num1, num2 = num2, temp

print(result)
