from functools import cache


def solve(data, n: int):
    data = tuple(tuple(map(int, v.split(","))) for v in data)

    def init_set(t) -> set:
        s = set()
        s.add(t)
        return s

    graph = [init_set(t) for t in data]

    def find_set(val) -> set:
        for se in graph:
            if val in se:
                graph.remove(se)
                return se

    for _, t1, t2 in get_closest(data, n):
        set1 = find_set(t1)
        if t2 in set1:
            graph.append(set1)
            continue

        set2 = find_set(t2)
        graph.append(set1.union(set2))

    return eval("*".join(map(str, sorted(len(n) for n in graph)[-3:])))


def get_closest(data, n: int):
    vals = []
    for idx, o in enumerate(data):
        for t in data[idx:]:
            if t == o:
                continue
            vals.append((get_dist(o, t), o, t))
    return sorted(vals)[:n]


@cache
def get_dist(orig: tuple[int], target: tuple[int]) -> int:
    return sum((o - t) ** 2 for o, t in zip(orig, target)) ** 0.5


if __name__ == "__main__":
    exp = [
        "162,817,812",
        "57,618,57",
        "906,360,560",
        "592,479,940",
        "352,342,300",
        "466,668,158",
        "542,29,236",
        "431,825,988",
        "739,650,466",
        "52,470,668",
        "216,146,977",
        "819,987,18",
        "117,168,530",
        "805,96,715",
        "346,949,466",
        "970,615,88",
        "941,993,340",
        "862,61,35",
        "984,92,344",
        "425,690,689",
    ]
    assert solve(exp, 10) == 40

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA, 1000))
