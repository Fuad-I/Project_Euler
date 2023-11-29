def lattice(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    output = [1]
    temp = lattice(n-1)
    for i in range(len(temp)-1):
        output.append(temp[i]+temp[i+1])
    output.append(1)
    return output


ans = lattice(40)
print(ans[len(ans)//2])
