from copy import deepcopy

matrix = list()
with open('p082_matrix.txt', 'r') as file:
    for line in file:
        matrix.append([int(x) for x in line.split(',')])

n = len(matrix)
distance_matrix = [matrix[i][0] for i in range(n)]

for col in range(1, n):
    column = [matrix[i][col] for i in range(n)]
    distance_matrix = [column[row] + min([distance_matrix[prev_row] + sum(
                                        column[prev_row:row: (1 if prev_row <= row else -1)]
                                        ) for prev_row in range(n)])
                       for row in range(n)]

print(min(distance_matrix))
