from itertools import combinations


def solve(points: list[str]):
    points = [tuple(map(int, p.split(","))) for p in points]
    squares = []
    for p1, p2 in combinations(points, 2):
        squares.append((calc_area(p1, p2)))
    return max(squares)


def calc_area(p1: tuple[int], p2: tuple[int]) -> int:
    return abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)


if __name__ == "__main__":
    exp = ["7,1", "11,1", "11,7", "9,7", "9,5", "2,5", "2,3", "7,3"]
    assert solve(exp) == 50

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
