i = 11
while True:
    if sorted([int(x) for x in str(i)]) == sorted([int(x) for x in str(i * 2)]) == sorted([int(x) for x in str(i * 3)]) == \
            sorted([int(x) for x in str(i * 4)]) == sorted([int(x) for x in str(i * 5)]) == sorted([int(x) for x in str(i * 6)]):
        print('Answer found:', i)
        break
    else:
        print(i)
        i += 1

