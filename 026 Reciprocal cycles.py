def fractionToDecimal(numr, denr):
    res = ""

    mp = {}
    rem = numr % denr

    while (rem != 0) and (rem not in mp):
        # Store this remainder
        mp[rem] = len(res)

        # Multiply remainder with 10
        rem = rem * 10

        # Append rem / denr to result
        res_part = rem // denr
        res += str(res_part)

        # Update remainder
        rem = rem % denr

    if rem == 0:
        return ""
    else:
        return res[mp[rem]:]


l = 0
number = 0
for i in range(2, 1000):
    rec_decimal = fractionToDecimal(1, i)
    if len(str(rec_decimal)) > l:
        l, number = len(str(num)), i

print(l, number)
