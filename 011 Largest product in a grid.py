from math import prod
from collections import OrderedDict

input_matrix = []

with open('p011.txt', 'r') as file:
    for line in file:
        input_matrix.append([int(i) for i in line.split()])


def matrix_max_prod(matrix, n):
    return max(max_vertical_prod(matrix, n), max_horizontal_prod(matrix, n), max_diagonal_product(matrix, n))


def lst_max_prod(lst, n):
    max_val = 0
    for i in range(len(lst) - n):
        if prod(lst[i:i + n]) > max_val:
            max_val = prod(lst[i:i + n])

    return max_val


def max_vertical_prod(matrix, n):
    return max_horizontal_prod(transpose(matrix), n)


def max_horizontal_prod(matrix, n):
    max_val = 0
    for lst in matrix:
        if lst_max_prod(lst, n) > max_val:
            max_val = lst_max_prod(lst, n)

    return max_val


def transpose(matrix):
    output = list()
    for i in range(len(matrix[0])):
        output.append([lst[i] for lst in matrix])
    return output


def max_diagonal_product(matrix, n):
    max_val = 0
    for lst in diagonals(matrix):
        if len(lst) >= n:
            if lst_max_prod(lst, n) > max_val:
                max_val = lst_max_prod(lst, n)
    return max_val


def diagonals(matrix):
    diagonal_matrix = list()
    for i in range(len(matrix)):
        diagonal_matrix.append([matrix[j][j + i] for j in range(len(matrix) - i)])
        diagonal_matrix.append([matrix[j + i][j] for j in range(len(matrix) - i)])
    row_reversed_matrix = [list(reversed(lst)) for lst in matrix]
    for i in range(len(row_reversed_matrix)):
        diagonal_matrix.append([row_reversed_matrix[j][j + i] for j in range(len(row_reversed_matrix) - i)])
        diagonal_matrix.append([row_reversed_matrix[j + i][j] for j in range(len(row_reversed_matrix) - i)])

    row_reversed_matrix = set([tuple(item) for item in diagonal_matrix])
    return [list(item) for item in list(row_reversed_matrix)]


print(matrix_max_prod(input_matrix, 4))
