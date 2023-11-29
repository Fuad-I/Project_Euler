num1 = 1504170715041707
num2 = 4503599627370517

eulercoins = [1504170715041707, 8912517754604]

while True:
    temp1 = eulercoins[-1]
    temp2 = eulercoins[-2]
    if temp1 < 2:
        break
    i = 2
    while True:
        if temp1 * i % temp2 < eulercoins[-1]:
            eulercoins.append(temp1 * i % temp2)
            break
        i += 1

print(sum(eulercoins), eulercoins)
