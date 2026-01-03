import sys
import itertools
import shapely

points = [list(map(int, line.split(','))) for line in sys.stdin.readlines()]


def part1():
    print(max([(abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1) for p1, p2 in itertools.combinations(points, 2)]))


def part2():

    polygon = shapely.Polygon(points)
    res = 0

    for p1, p2 in itertools.combinations(points, 2):

        x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
        y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
        area = (x_max - x_min + 1) * (y_max - y_min + 1)

        if polygon.contains(shapely.box(x_min, y_min, x_max, y_max)):
            res = max(area, res)

    print(res)


part1()
part2()
