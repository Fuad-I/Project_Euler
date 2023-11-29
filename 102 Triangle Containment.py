matrix = list()

with open('p102_triangles.txt', 'r') as file:
    for line in file:
        matrix.append([int(x) for x in line.split(',')])


def triangle_area(A, B, C):
    return abs((A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])) * 0.5)


origin = (0, 0)


def solve(input_matrix):
    return sum(
        [triangle_area(lst[0:2], lst[2:4], lst[4:6]) == triangle_area(lst[0:2], origin, lst[2:4]) +
         triangle_area(lst[0:2], origin, lst[4:6]) + triangle_area(lst[2:4], origin, lst[4:6])
         for lst in input_matrix]
    )


print(solve(matrix))