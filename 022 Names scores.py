names_list = list()
with open('names.txt', 'r') as file:
    for line in file:
        names_list.extend([word.strip('""') for word in line.split(',')])

names_list = sorted(names_list)

total = 0
for i in range(len(names_list)):
    total += sum(ord(letter.lower())-96 for letter in names_list[i]) * (i+1)

print(total)
