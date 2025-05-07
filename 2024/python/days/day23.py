from collections import defaultdict


def solve() -> tuple[int, int]:
    get_data(False)
    p1 = len(find_groups())
    # p2 = find_largest()
    p2 = ",".join(
        sorted(bron_kerbosch(set(), set(find_related()), set(), find_related()))
    )
    return (p1, p2)


def find_largest():
    related = find_related()

    groups = set()
    for mem1, set_mem in related.items():
        for sub_mem in set_mem:
            joined = ",".join(sorted([mem1, *list(set_mem & related[sub_mem])]))
            groups.add(joined)
    print(groups)


def bron_kerbosch(result, source, exclude, related):
    if not source and not exclude:
        return result

    max_clique = set()
    for vertex in source.copy():
        clique = bron_kerbosch(
            result.union({vertex}),
            source & related[vertex],
            exclude & related[vertex],
            related,
        )
        max_clique = max(max_clique, clique, key=len)
        source.remove(vertex)
        exclude.add(vertex)
    return max_clique


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
