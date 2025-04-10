def solve() -> tuple[int, int]:
    global Marked
    get_data(False)
    Marked = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

    p1 = part_1(False)
    p2 = part_1(True)
    return (p1, p2)


def part_1(ispart2):
    price = 0
    for idx, line in enumerate(DATA):
        for idy, char in enumerate(line):
            if Marked[idx][idy]:
                continue
            area, perimeter = breath_search(idx, idy, char, 0, ispart2)
            price += area * perimeter
    return price


def breath_search(
    idx: int, idy: int, search_char: str, direction: int, ispart2: bool
) -> tuple[int, int]:
    """
    Returning tuple = (area, perimeter)
    """
    global Marked
    lhs, rhs = DIRECTION_DICT[direction]
    idx += lhs
    idy += rhs

    # Out of bounds perimeter
    if not (0 < idx + 1 <= SIZE) or not (0 < idy + 1 <= SIZE):
        if ispart2:
            return check_neighbor(idx, idy, search_char, direction)
        return (0, 1)

    # Backtracking results in nothing
    if DATA[idx][idy] == search_char:
        if Marked[idx][idy]:
            return (0, 0)
        Marked[idx][idy] = 1
    else:
        if ispart2:
            return check_neighbor(idx, idy, search_char, direction)
        return (0, 1)

    own_return_par = [1, 0]
    for dir in range(1, 5):
        area, perimeter = breath_search(idx, idy, search_char, dir, ispart2)
        own_return_par[0] += area
        own_return_par[1] += perimeter
    return tuple(own_return_par)


def check_limit(idx: int, idy: int, direction: int, search_char: str) -> bool:
    returns = []
    match direction:
        case 1 | 2:
            returns.append(check_neighbor(idx, idy + 1, search_char, direction))
            returns.append(check_neighbor(idx, idy - 1, search_char, direction))
        case 3 | 4:
            returns.append(check_neighbor(idx + 1, idy, search_char, direction))
            returns.append(check_neighbor(idx - 1, idy, search_char, direction))


def check_neighbor(idx: int, idy: int, search_char: str, direction: int) -> bool:
    try:
        if Marked[idx][idy] and DATA[idx][idy] == search_char:
            x, y = DIRECTION_DICT[direction]  # The change to indexes
            if DATA[idx + x][idy + y] != search_char:
                return (0, 1)

    except KeyError:
        return (0, 0)
    return (0, 0)


DIRECTION_DICT = {0: (0, 0), 1: (1, 0), 2: (-1, 0), 3: (0, 1), 4: (0, -1)}


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
