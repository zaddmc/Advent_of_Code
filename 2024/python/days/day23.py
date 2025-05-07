from collections import defaultdict


def solve() -> tuple[int, int]:
    get_data(False)
    p1 = len(find_groups())
    p2 = find_largest()
    return (p1, p2)


def find_largest():
    related = find_related()
    return -1


def find_groups():
    related = find_related()
    candidates = [c for c in related if c.startswith("t")]
    groups = set()

    for t in candidates:
        for a in related[t]:
            for b in related[a]:
                if b in related[t]:
                    groups.add(tuple(sorted([t, a, b])))
    return groups


def find_related():
    groups = defaultdict(set)
    for com1, com2 in DATA:
        groups[com1].add(com2)
        groups[com2].add(com1)
    return groups


def get_data(test: bool):
    global DATA
    if test:
        with open("../../input/day23exp.txt") as file:
            DATA = list(map(lambda s: s.split("-"), file.read().splitlines()))
    else:
        with open("../../input/day23.txt") as file:
            DATA = list(map(lambda s: s.split("-"), file.read().splitlines()))


if __name__ == "__main__":
    print(solve())
