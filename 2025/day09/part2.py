from functools import cache
from itertools import combinations


def solve(points: list[str]):
    points = tuple(tuple(map(int, p.split(","))) for p in points)

    squares = []
    for p1, p2 in combinations(points, 2):
        p3, p4 = other_points(p1, p2)
        if all(point_in_orthogonal_polygon(points, p) for p in [p3, p4]):
            squares.append((calc_area(p1, p2), p1, p2, p3, p4))
    print(sorted(squares))
    return max(squares)[0]


def AABB_collsion(polygon, point):
    return 1


@cache
def point_on_segment(px, py, x1, y1, x2, y2):
    if y1 == y2:
        if py != y1:
            return False
        return min(x1, x2) <= px <= max(x1, x2)
    if x1 == x2:
        if px != x1:
            return False
        return min(y1, y2) <= py <= max(y1, y2)
    return False


@cache
def point_in_orthogonal_polygon(polygon, point):
    px, py = point
    wn = 0
    N = len(polygon)

    for i in range(N):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % N]

        if point_on_segment(px, py, x1, y1, x2, y2):
            return True

        if y1 <= py < y2:
            if x1 > px:
                wn += 1

        elif y2 <= py < y1:
            if x1 > px:
                wn -= 1
    return wn != 0


def calc_area(p1: tuple[int], p2: tuple[int]) -> int:
    return abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)


def other_points(p1: tuple[int], p2: tuple[int]):
    return (p2[0], p1[1]), (p1[0], p2[1])


if __name__ == "__main__":
    exp = ["7,1", "11,1", "11,7", "9,7", "9,5", "2,5", "2,3", "7,3"]
    assert solve(exp) == 24

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
