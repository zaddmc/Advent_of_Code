import re
import sys
from random import shuffle

sys.setrecursionlimit(100000000)


def solve() -> tuple[int, int]:
    get_data(True)
    p1 = len(find_uniques(MOLECULE))
    p2 = random_shit()
    return (p1, p2)


def random_shit():
    global REPLACEMENTS
    target = MOLECULE
    depth = 0

    while target != "e":
        tmp = target
        for a, b in REPLACEMENTS:
            if b not in target:
                continue
            target.replace(b, a, 1)
            depth += 1

        if tmp == target:
            target = MOLECULE
            depth = 0
            shuffle(REPLACEMENTS)
    return depth


def find_uniques(curr):
    uniques = set()
    for re_key, re_val in REPLACEMENTS:

        prev_index = 0
        for _ in range(curr.count(re_key)):
            index = curr.find(re_key, prev_index)
            uniques.add(curr[:index] + curr[index:].replace(re_key, re_val, 1))

            prev_index = index + 1
    return uniques


def get_data(test: bool):
    global REPLACEMENTS, MOLECULE
    if test:
        with open("../../input/day19.exp.txt", "r") as file:
            data = file.read().splitlines()
    else:
        with open("../../input/day19.txt", "r") as file:
            data = file.read().splitlines()

    REPLACEMENTS = list(
        map(lambda s: s.split(), map(lambda s: s.replace("=> ", ""), data[:-2]))
    )
    MOLECULE = data[-1]


if __name__ == "__main__":
    print(solve())
