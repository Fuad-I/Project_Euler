def is_triplet(a, b, s):
    c = s - a - b
    while c > b:
        if a ** 2 + b ** 2 == c ** 2:
            return [a, b, c]
        else:
            b += 1
            c -= 1

    return False


result = 1
for i in range(1, 500):
    output = is_triplet(i, i, 1000)
    if output:
        print(output)
        for item in output:
            result *= item
        break

print(result)
