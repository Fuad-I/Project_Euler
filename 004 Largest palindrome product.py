max_val = 0
for i in range(999, 100, -1):
    for j in range(i-1, 100, -1):
        if str(i*j) == str(i*j)[-1::-1] and i*j > max_val:
            max_val = i*j
            break
print(max_val)
