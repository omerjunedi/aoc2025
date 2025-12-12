import sys
D = sys.stdin.read()

res = 0
for bank in D.splitlines():

    str_bank = str(bank)
    left_digit = ""
    ind = 0
    for i in range(9, -1, -1):
        if str(i) in str_bank and (ind := str_bank.find(str(i))) != len(str_bank) - 1:
            left_digit = str(i)
            break

    right_digit = max(str_bank[ind+1:])
    a = left_digit + right_digit
    num = int(a)
    res += num



res = 0
for bank in D.splitlines():
    digits: list[str] = []
    str_bank = str(bank)
    n = len(str_bank)
    prev = 0
    for remain in range(12, 0, -1):
        end = n - remain + 1
        digits.append(best := (max(str_bank[prev:end])))
        prev = str_bank.index(best, prev, end) + 1

    a = "".join(digits)
    res += int(a)


print(res)
