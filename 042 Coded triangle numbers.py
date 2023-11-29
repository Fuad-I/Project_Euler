word_list = list()
with open('file.txt', 'r') as file:
    for line in file:
        word_list.extend(line.split(','))

for i in range(len(word_list)):
    word_list[i] = word_list[i].strip('""')

max_word_len = max([len(x) for x in word_list])    # get the length of the longest word
triangle_numbers = [n*(n+1)//2 for n in range(1, 28)]

count = 0
for item in word_list:
    if sum([ord(x.lower())-96 for x in item]) in triangle_numbers:
        count += 1

print(count)
