def solve() -> tuple[int, int]:
    global Marked
    get_data(False)
    Marked = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

    p1 = part_1()
    return (p1, -1)


def part_1():
    price = 0
    for idx, line in enumerate(DATA):
        for idy, char in enumerate(line):
            if Marked[idx][idy]:
                continue
            area, perimeter = breath_search(idx, idy, char)
            price += area * perimeter
    return price


def breath_search(idx: int, idy: int, search_char: str) -> tuple[int, int]:
    """
    Returning tuple = (area, perimeter)
    """
    global Marked
    # Out of bounds perimeter
    if not (0 < idx + 1 <= SIZE) or not (0 < idy + 1 <= SIZE):
        return (0, 1)

    # Backtracking results in nothing
    if DATA[idx][idy] == search_char:
        if Marked[idx][idy]:
            return (0, 0)
        Marked[idx][idy] = 1
    else:
        return (0, 1)

    next_search = [
        breath_search(idx + 1, idy, search_char),
        breath_search(idx - 1, idy, search_char),
        breath_search(idx, idy + 1, search_char),
        breath_search(idx, idy - 1, search_char),
    ]
    own_return_par = [1, 0]
    for elm in next_search:
        own_return_par[0] += elm[0]
        own_return_par[1] += elm[1]
    return tuple(own_return_par)


def check_limit(idx: int, idy: int, direction: int, search_char: str) -> bool:
    pass


def check_neighbor(idx: int, idy: int, search_char: str, direction: int) -> bool:
    try:
        if Marked[idx][idy] and DATA[idx][idy] == search_char:
            x, y = DIRECTION_DICT[direction]  # The change to indexes
            if DATA[idx + x][idy + y] != search_char:
                return (0, 1)

    except KeyError:
        return (0, 0)


DIRECTION_DICT = {1: (1, 0), 2: (-1, 0), 3: (0, 1), 4: (0, -1)}


def pr_marked():
    for line in Marked:
        print(line)


def get_data(test: bool = False):
    global DATA, SIZE
    if test:
        DATA = [
            "RRRRIICCFF",
            "RRRRIICCCF",
            "VVRRRCCFFF",
            "VVRCCCJFFF",
            "VVVVCJJCFE",
            "VVIVCCJJEE",
            "VVIIICJJEE",
            "MIIIIIJJEE",
            "MIIISIJEEE",
            "MMMISSJEEE",
        ]
    else:
        with open("../../input/day12.txt", "r") as file:
            DATA = file.read().strip().split()
    SIZE = len(DATA)
    return DATA


if __name__ == "__main__":
    print(solve())
