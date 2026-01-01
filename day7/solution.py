from functools import cache
import sys

D = sys.stdin.read().splitlines()

start = D[0].index('S')
N = len(D)
M = len(D[0])


def part1(row: int, col: int, visited: set[tuple[int, int]], res: list[int]) -> None:

    if col not in range(M):
        return

    if row not in range(N):
        return

    for r in range(row, N):
        if D[r][col] == '^':
            if (r, col) not in visited:
                res[0] += 1
                visited.add((r, col))
                part1(r+1, col-1, visited, res)
                part1(r+1, col+1, visited, res)
            return


@cache
def part2(row: int, col: int) -> int:

    # complete path
    if row == N - 1:
        return 1

    if col not in range(M):
        return 0

    if row not in range(N):
        return 0

    for r in range(row, N):
        if D[r][col] == '^':
            return part2(r+1, col-1) + part2(r+1, col+1)

    return 1



res = [0]
visited: set[tuple[int, int]] = set()
part1(0, start, visited, res)
print(res[0])

print(part2(0, start))
