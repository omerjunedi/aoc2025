import sys

D = sys.stdin.read().splitlines()

start = D[0].index('S')
N = len(D)
M = len(D[0])


def recurse(row: int, col: int, visited: set[tuple[int, int]], res: list[int]) -> None:

    if col not in range(M):
        return

    if row not in range(N):
        return

    for r in range(row, N):
        if D[r][col] == '^':
            if (r, col) not in visited:
                res[0] += 1
                visited.add((r, col))
                recurse(r+1, col-1, visited, res)
                recurse(r+1, col+1, visited, res)
            return


res = [0]
visited: set[tuple[int, int]] = set()

recurse(0, start, visited, res)
print(res[0])
