import sys
D = sys.stdin.read().splitlines()
ranges = D[:(a := D.index(''))]
ids = D[a+1:]
int_ranges = [[0, 0] for _ in range(len(ranges))]

for i, val in enumerate(ranges):
    start, end = map(int, val.split('-'))
    int_ranges[i] = [start, end]


def merge(intervals: list[list[int]]) -> list[list[int]]:

    merged: list[list[int]] = []
    intervals.sort(key=lambda x: x[0])

    prev = intervals[0]

    for interval in intervals[1:]:

        if interval[0] <= prev[1]:
            prev[1] = max(prev[1], interval[1])

        else:

            merged.append(prev)
            prev = interval

    merged.append(prev)
    return merged


merged_intervals = merge(int_ranges)
res = 0
for a, b in merged_intervals:
    res += (b - a + 1)

print(f"part 2: {res}")

# part 1
res = 0
for id in ids:
    inside = False
    for x, y in int_ranges:
        if int(id) in range(x, y):
            res += 1
            inside = True
            break

print(f"part 1: {res}")
