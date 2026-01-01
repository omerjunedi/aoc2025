import sys
from math import sqrt
from itertools import combinations
type Point = tuple[int, int, int]
points: list[Point] = [tuple(map(int, line.split(','))) for line in sys.stdin.readlines()]


def calc_dist(p1: Point, p2: Point) -> float:
    x, y, z = p1
    xp, yp, zp = p2
    return sqrt(abs(x-xp) ** 2 + abs(y-yp) ** 2 + abs(z-zp) ** 2)


closest_points: list[tuple[float, Point, Point]] = []

for p1, p2 in combinations(points, 2):
    dist = calc_dist(p1, p2)
    closest_points.append((dist, p1, p2))

closest_points.sort(reverse=True)

# list of sets, each set represents a circuit
# can easily check inclusion and combining two circuits into one, a.union(b), a.clear() where a and b are sets

# keep a map of point to index of set it is contained in
pointCircuitMap: dict[Point, int] = {}
circuits: list[set[Point]] = []
c = 0

for _, p1, p2 in reversed(closest_points):

    if p1 in pointCircuitMap and p2 in pointCircuitMap:
        if pointCircuitMap[p1] != pointCircuitMap[p2]:
            a = min(pointCircuitMap[p1], pointCircuitMap[p2])
            b = max(pointCircuitMap[p1], pointCircuitMap[p2])
            circuits[a] = circuits[a].union(circuits[b])
            pointCircuitMap[p2] = a
            for p in circuits[b]:
                pointCircuitMap[p] = a
            circuits[b].clear()

    if p1 in pointCircuitMap and p2 not in pointCircuitMap:
        pointCircuitMap[p2] = pointCircuitMap[p1]
        circuits[pointCircuitMap[p1]].add(p2)

    if p2 in pointCircuitMap and p1 not in pointCircuitMap:
        pointCircuitMap[p1] = pointCircuitMap[p2]
        circuits[pointCircuitMap[p2]].add(p1)

    if p1 not in pointCircuitMap and p2 not in pointCircuitMap:
        circuits.append({p1, p2})
        pointCircuitMap[p1] = len(circuits) - 1
        pointCircuitMap[p2] = len(circuits) - 1

    c += 1
    if c == 1000:
        break

circuits.sort(key=len, reverse=True)
print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))
