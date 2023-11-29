def n_th_digit(num, n):
    temp = [x for x in str(num)]
    return int(temp[n-1])


def remove_first(num):
    temp = [x for x in str(num)]
    temp.pop(0)
    return int(''.join(temp))


nums = [129, 160, 162, 168, 180, 289, 290, 316, 318, 319, 362, 368, 380, 389, 620, 629, 680, 689, 690, 710, 716, 718,
        719, 720, 728, 729, 731, 736, 760, 762, 769, 790, 890]

numbers = ''.join([str(x) for x in nums])
new_set = set([int(x) for x in numbers])
arr = []

while True:
    appear_first = set(n_th_digit(x, 1) for x in nums)
    appear_second = set(n_th_digit(x, 2) for x in nums)
    appear_third = set(n_th_digit(x, 3) for x in nums)
    first = appear_first - appear_second
    second = (appear_first | appear_second) - (appear_third | first)
    arr.extend([first, second])

    for i in range(len(nums)):
        if {n_th_digit(nums[i], 1)} == first or {n_th_digit(nums[i], 1)} == second:
            nums[i] = remove_first(nums[i])
    if len(arr) == 8:
        break

print(arr)
print(nums)
