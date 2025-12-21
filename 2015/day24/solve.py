from functools import reduce
from itertools import combinations
from operator import mul


def solve(data, buckets):
    target = sum(data) // buckets

    for n in range(1, len(data)):
        solutions = [
            reduce(mul, x) for x in tuple(combinations(data, n)) if sum(x) == target
        ]
        if solutions:
            return min(solutions)


if __name__ == "__main__":

    with open("input.txt", "r") as file:
        DATA = tuple(map(int, file.read().strip().splitlines()))
    p1 = solve(DATA, 3)
    p2 = solve(DATA, 4)
    print(p1, p2)
