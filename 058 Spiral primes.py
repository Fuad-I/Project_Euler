from functions import is_prime

prime = 0
side = 3
while True:
    prime += is_prime((side-1)*side + 1)
    prime += is_prime((side - 2) * side + 2)
    prime += is_prime((side - 3) * side + 3)
    if (side * 2 - 1 - prime) / prime > 9:
        break
    side += 2
print(side)
