matrix = list()
with open('p081_matrix.txt', 'r') as file:
    for line in file:
        matrix.append([int(x) for x in line.split(',')])


def get_diagonal_matrix(input_matrix: list) -> list:
    output = list()
    for i in range(1, len(input_matrix)):
        output.append([input_matrix[i - 1 - j][j] for j in range(i)])

    for i in range(len(input_matrix)):
        output.append([input_matrix[-1 - j][j + i] for j in range(len(input_matrix) - i)])

    return output


diagonal_matrix = get_diagonal_matrix(matrix)
diagonal_matrix.reverse()

for i in range(1, len(diagonal_matrix) // 2 + 1):
    diagonal_matrix[i][0] += diagonal_matrix[i - 1][0]
    diagonal_matrix[i][-1] += diagonal_matrix[i - 1][-1]
    for j in range(1, len(diagonal_matrix[i]) - 1):
        diagonal_matrix[i][j] = diagonal_matrix[i][j] + min(diagonal_matrix[i - 1][j], diagonal_matrix[i - 1][j - 1])

for i in range(len(diagonal_matrix) // 2 + 1, len(diagonal_matrix)):
    for j in range(len(diagonal_matrix[i])):
        diagonal_matrix[i][j] += min(diagonal_matrix[i - 1][j], diagonal_matrix[i - 1][j + 1])

print(diagonal_matrix)


def calc(input_matrix):
    for i in range(1, len(input_matrix) // 2 + 1):
        input_matrix[i][0] += input_matrix[i - 1][0]
        input_matrix[i][-1] += input_matrix[i - 1][-1]
        for j in range(1, len(input_matrix[i]) - 1):
            input_matrix[i][j] = input_matrix[i][j] + min(input_matrix[i - 1][j],
                                                          input_matrix[i - 1][j - 1])
    for i in range(len(input_matrix) // 2 + 1, len(input_matrix)):
        for j in range(len(input_matrix[i])):
            input_matrix[i][j] += min(input_matrix[i - 1][j], input_matrix[i - 1][j + 1])


temp = [[17], [21, 13], [11, 22, 15]]
temp2 = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956],
         [605, 732, 524, 37, 331]]

"""for i in range(3):
    min_num = min(num for l in temp2 for num in l)
    for row in temp2:
        for col in row:
            row[row.index(col)] -= min_num
        for item in temp2:
            if 0 in item:
                item.remove(0)
        print(temp2)
# print(temp2) """


def func(input):
    min_num = min(min(item) for item in input)
    for lst in input:
        for i in range(len(lst)):
            lst[i] -= min_num
        if 0 in lst:
            lst.remove(0)


def solve():
    while True:
        for lst in temp2:
            if len(lst) == 1:
                return temp2
        func(temp2)


print(solve())
