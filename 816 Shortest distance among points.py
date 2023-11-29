"""lst = [290797]
for i in range(2000000-1):
    lst.append(lst[-1] ** 2 % 50515093)

print(len(set(lst)))"""


def romanToInt(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    """lst = [d[s[-1]]]
    for i in range(1, len(s)):
        if d[s[-1-i]] < lst[-1]:
            lst.append(-d[s[-1-i]])
        else:
            lst.append(d[s[-1-i]])
    return sum(lst) """
    total = d[s[-1]]
    temp = d[s[-1]]
    for i in range(1, len(s)):
        if d[s[-1 - i]] < temp:
            total -= d[s[-1 - i]]
        else:
            total += d[s[-1 - i]]
    return total
