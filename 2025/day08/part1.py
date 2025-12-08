from functools import cache


def solve(data, n: int):
    data = tuple(tuple(map(int, v.split(","))) for v in data)

    connections = set()

    for _ in range(n):
        pair = find_the_closest(data, connections)
        connections.add(pair)

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

    for t1, t2 in connections:
        set1 = find_set(t1)
        if t2 in set1:
            graph.append(set1)
            continue

        set2 = find_set(t2)

        graph.append(set1.union(set2))

    print("Finished")
    return eval("*".join(map(str, sorted(len(n) for n in graph)[-3:])))


def find_the_closest(data: tuple[tuple[int]], connections: set):
    def find_closest(orig: tuple[int], begin: int):
        clostset_junc = None
        clostset_dist = 999999999

        for target in data[begin:]:
            if target == orig:
                continue
            if (target, orig) in connections:
                continue

            dist = get_dist(orig, target)
            if dist < clostset_dist:
                clostset_dist = dist
                clostset_junc = target
        return clostset_dist, clostset_junc

    return min((*find_closest(t, idx), t) for idx, t in enumerate(data))[1:]


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
