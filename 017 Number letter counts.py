one_to_nine = (3, 3, 5, 4, 4, 3, 5, 5, 4)
ten_to_nineteen = (3, 6, 6, 8, 8, 7, 7, 9, 8, 8)
twenty_ninety = (6, 6, 5, 5, 5, 7, 6, 6)

sum1 = sum(one_to_nine) + sum(ten_to_nineteen)  # 1-19
sum1 += sum(item * 10 + sum(one_to_nine) for item in twenty_ninety)   # 1-19 + 20-99

result = sum(item + 7 + (item + 10) * 99 + sum1 for item in one_to_nine) + 11 + sum1
print(result)
