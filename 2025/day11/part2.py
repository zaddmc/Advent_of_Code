from functools import cache


def solve(data):
    graph = {}
    for d in data:
        k, v = d.split(": ")
        graph[k] = tuple(v.split())
    res = find_paths(graph)
    return res


def find_paths(graph: tuple):
    @cache
    def find_path(key: str, v_dac: bool, v_fft: bool):
        match key:
            case "out":
                return 1 if v_dac and v_fft else 0
            case "dac":
                v_dac = True
            case "fft":
                v_fft = True
        paths = 0
        for val in graph[key]:
            paths += find_path(val, v_dac, v_fft)
        return paths

    return find_path("svr", False, False)


if __name__ == "__main__":
    exp = [
        "svr: aaa bbb",
        "aaa: fft",
        "fft: ccc",
        "bbb: tty",
        "tty: ccc",
        "ccc: ddd eee",
        "ddd: hub",
        "hub: fff",
        "eee: dac",
        "dac: fff",
        "fff: ggg hhh",
        "ggg: out",
        "hhh: out",
    ]
    assert solve(exp) == 2

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
