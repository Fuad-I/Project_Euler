from functions import gcd, lcd


def sum_of_multiples_one(num, limit):
    return limit // num * (limit // num + 1) * num // 2


def sum_of_multiples_two(num1, num2, limit):
    if max(num1, num2) % min(num1, num2) == 0:
        return sum_of_multiples_one(max(num1, num2), limit)
    return sum_of_multiples_one(num1, limit) + sum_of_multiples_one(num2, limit) \
        - sum_of_multiples_one(lcd(num1, num2), limit)


def sum_of_multiples(limit, *args):
    ans = sum(sum_of_multiples_one(item, limit) for item in args)
    lst = list(args)
    for i in range(len(lst)):
        for item in lst[i+1:]:
            ans -= sum_of_multiples_one(lcd(lst[i], item), limit)

    return ans


print(sum_of_multiples_two(3, 5, 1000))
print(sum_of_multiples_two(9, 15, 92))
print(gcd(9,15), lcd(9,15))
print(sum_of_multiples_one(9, 92))
print(sum_of_multiples_one(6, 92))
print(sum_of_multiples(92, 6, 9, 15))
