from collections import defaultdict
from itertools import permutations


def solve() -> tuple[int, int]:
    get_data()
    paths = list(brute_force())
    p1 = min(paths)
    p2 = max(paths)
    return (p1, p2)


def brute_force():
    graph, cost = init_paths()

    for perm in permutations(graph.keys()):
        dist = 0
        for i in range(len(perm) - 1):
            dist += [
                int(line[-1])
                for line in DATA
                if perm[i] in line and perm[i + 1] in line
            ][0]
        yield dist


def init_paths():
    paths = {}
    graph = defaultdict(list)

    for a, b, dist in DATA:
        paths[tuple(sorted((a, b)))] = int(dist)
        graph[a].append(b)
        graph[b].append(a)
    return graph, paths


def get_data():
    global DATA
    with open("../../input/day09.txt", "r") as file:
        DATA = list(
            map(
                lambda s: s.split(" "),
                file.read().replace(" to", "").replace(" =", "").splitlines(),
            )
        )


if __name__ == "__main__":
    print(solve())
