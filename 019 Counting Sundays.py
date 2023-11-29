months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = (1 + sum(months)) % 7
count = 0

for year in range(1901, 2001):
    for month in months:
        if month == 28 and year % 4 == 0:
            day += month + 1
        else:
            day += month

        if day % 7 == 0:
            count += 1
print(count)
