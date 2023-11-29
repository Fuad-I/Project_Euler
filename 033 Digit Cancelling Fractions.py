from functions import reduce_fraction


new_list1 = list()
new_list2 = list()
count = 0
for i in range(11, 100):
    for j in range(i + 1, 100):
        if i % 10 == 0 or j % 10 == 0:
            continue

        if str(i)[0] == str(j)[1]:
            if int(str(i)[1]) / int(str(j)[0]) == i/j:
                count += 1
                new_list1.append(i)
                new_list2.append(j)
        elif str(i)[1] == str(j)[0]:
            if int(str(i)[0]) / int(str(j)[1]) == i/j:
                count += 1
                new_list1.append(i)
                new_list2.append(j)

numerator = 1
denominator = 1

for i in range(4):
    numerator *= new_list1[i]
    denominator *= new_list2[i]

print(reduce_fraction(numerator, denominator))
