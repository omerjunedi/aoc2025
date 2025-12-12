import sys

D = sys.stdin.readline().strip()

res = 0
for window in D.split(','):
    start, end = map(int, window.split('-'))
    for num in range(start, end + 1):
        str_num = str(num)

        if len(str_num) % 2 != 0:
            continue

        if str_num[len(str_num)//2:] == str_num[:len(str_num)//2]:
            res += num

print(f"Part 1: {res}")

res = 0
for window in D.split(','):
    start, end = map(int, window.split('-'))
    for num in range(start, end + 1):
        str_num = str(num)
        for i in range(1, len(str_num)//2 + 1):
            quotient, remainder = divmod(len(str_num), i)
            if remainder == 0 and str_num[:i] * quotient == str_num:
                res += num
                break



print(f"Part 2: {res}")
