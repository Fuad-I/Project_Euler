from functions import is_prime

lst = [x for x in range(1001, 10000) if is_prime(x)]
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if 2*lst[j] - lst[i] in lst:
            if sorted(str(lst[i])) == sorted(str(lst[j])) == sorted(str(2*lst[j] - lst[i])):
                print(lst[i], lst[j], 2*lst[j] - lst[i])
