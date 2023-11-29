# (n*(n+1)//2)**2 - n*(n+1)*(2*n+1)//6 == n*(n+1)//2 * (n*(n+1)//2 - (2*n+1)//3)

def sum_square_difference(n):
    return n*(n+1)//2 * (n*(n+1)//2 - (2*n+1)//3)


print(sum_square_difference(100))
