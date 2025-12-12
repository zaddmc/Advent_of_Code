from heapq import heappop, heappush


def solve(data):
    graph = {}
    for d in data:
        k, v = d.split(": ")
        graph[k] = tuple(v.split())
    res = find_paths(graph)
    return res


def find_paths(graph: tuple):
    not_visited = [(0, "you")]
    paths = 0

    while not_visited:
        c, key = heappop(not_visited)
        c += 1

        for val in graph[key]:
            if val == "out":
                paths += 1
                break
            heappush(not_visited, (c, val))
    return paths


if __name__ == "__main__":
    exp = [
        "aaa: you hhh",
        "you: bbb ccc",
        "bbb: ddd eee",
        "ccc: ddd eee fff",
        "ddd: ggg",
        "eee: out",
        "fff: out",
        "ggg: out",
        "hhh: ccc fff iii",
        "iii: out",
    ]
    assert solve(exp) == 5

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
