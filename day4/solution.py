import sys

D = sys.stdin.read()
grid: list[list[str]] = [list(line) for line in D.splitlines()]
N, M = len(grid), len(grid[0])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def in_bounds(x: int, y: int) -> bool:
    return x in range(N) and y in range(M)

res = 0
can_remove = True
while can_remove:
    can_remove = False
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '@':
                adjacent = 0
                for dx, dy in directions:
                    if in_bounds(i + dx, j + dy) and grid[i+dx][j+dy] == '@':
                        adjacent += 1

                if adjacent < 4:
                    res += 1
                    can_remove = True
                    grid[i][j] = '.'


print(res)
