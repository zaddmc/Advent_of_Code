from knot_hash import knot_hash


def solve(data):
    memory = []
    for num in range(128):
        ret = "".join(
            [
                f"{bin(val).removeprefix("0b"):>08}"
                for val in knot_hash(data + "-" + str(num))
            ]
        )
        memory.append(ret)

    visited = set()
    regions = 0
    for idx, row in enumerate(memory):
        for idy, item in enumerate(row):
            if item == "1" and (idx, idy) not in visited:
                regions += 1
                visited = fill_region(memory, visited, idx, idy)
    return regions


def fill_region(memory: list[str], visited: set, idx: int, idy: int):
    queue = []
    queue.extend(get_neigh(memory, idx, idy))
    while len(queue) != 0:
        ix, iy = queue.pop()
        if (ix, iy) not in visited:
            visited.add((ix, iy))
            queue.extend(get_neigh(memory, ix, iy))
    return visited


def get_neigh(memory: list[str], idx, idy):
    return [
        (ix, iy)
        for (ix, iy) in [(idx + 1, idy), (idx - 1, idy), (idx, idy + 1), (idx, idy - 1)]
        if 0 <= ix < 128 and 0 <= iy < 128 and memory[ix][iy] == "1"
    ]


if __name__ == "__main__":
    assert solve("flqrgnkx") == 1242

    with open("input.txt", "r") as file:
        print(solve(file.read().strip()))
