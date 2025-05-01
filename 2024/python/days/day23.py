from itertools import combinations


def solve() -> tuple[int, int]:
    get_data(True)
    print(len(find_groups()), find_groups())
    p1 = [group for group in find_groups() if "t" in group[::3]]
    return (p1, -1)


def find_groups():
    related = find_related()
    groups = set()
    for mem1, set_mem in related.items():
        for sub_mem in set_mem:
            joined = ",".join(sorted([mem1, *list(set_mem & related[sub_mem])]))
            if len(joined) > 8:
                for new_group in combinations(joined.split(","), 3):
                    groups.add(",".join(new_group))
            if len(joined) == 8:
                groups.add(joined)
    return groups


def find_related():
    groups = {}
    for com1, com2 in DATA:
        if com1 not in groups.keys():
            groups[com1] = set()
        groups[com1].add(com2)

        if com2 not in groups.keys():
            groups[com2] = set()
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
