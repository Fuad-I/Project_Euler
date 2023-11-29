class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.previous_left = None
        self.previous_right = None
        self.sum_list = list()


nodes_list = list()
num_list = list()
with open('p067_triangle.txt', 'r') as file:
    for line in file:
        num_list.append([int(x) for x in line.split()])
        # nodes_list.append([Node(int(x)) for x in line.split()])

"""i = 1
for list1 in nodes_list:
    j = 0
    for item in list1:
        item.left = nodes_list[i][j]
        item.right = nodes_list[i][j + 1]
        j += 1
    i += 1
    if i >= len(nodes_list):
        break


for lst in reversed(nodes_list):
    for item in lst:
        if item.left and item.right:
            item.data = item.data + max(item.left.data, item.right.data)
        elif item.left:
            item.data = item.data + item.left.data
        elif item.right:
            item.data = item.data + item.right.data

print(nodes_list[0][0].data) """

num_list.reverse()
for i in range(1, len(num_list)):
    for j in range(len(num_list[i])):
        num_list[i][j] += max(num_list[i - 1][j], num_list[i - 1][j + 1])

print(num_list[-1])
