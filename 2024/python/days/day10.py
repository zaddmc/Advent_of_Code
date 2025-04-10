def solve() -> tuple[int, int]:
    global DATA, SIZE
    DATA = get_data(False)
    SIZE = len(DATA)
    trails = {}
    for idx, line in enumerate(DATA):
        for idy, height in enumerate(line):
            if height == "0":
                new_trails = trails[(idx, idy)] = []
                find_trail(idx, idy, "0", new_trails)
    return (tally(trails), -1)


def get_data(test: bool = False):
    if test:
        return [
            "89010123",
            "78121874",
            "87430965",
            "96549874",
            "45678903",
            "32019012",
            "01329801",
            "10456732",
        ]

    return open("../../input/day10.txt", "r").read().strip().split()


def find_trail(idx: int, idy: int, next_val: str, trail_list: list):

    if not 0 < idx + 1 < SIZE + 1 or not 0 < idy + 1 < SIZE + 1:
        return

    if DATA[idx][idy] == "9" and next_val == "9":
        if (idx, idy) not in trail_list:
            trail_list.append((idx, idy))
        return

    if DATA[idx][idy] != next_val:
        return

    check = "0123456789"  # The next value to find
    new_next_val = check[check.index(next_val, 0, len(check)) + 1]
    find_trail(idx + 1, idy, new_next_val, trail_list)
    find_trail(idx - 1, idy, new_next_val, trail_list)
    find_trail(idx, idy + 1, new_next_val, trail_list)
    find_trail(idx, idy - 1, new_next_val, trail_list)
    return


def tally(trail_dict: dict[tuple, list[tuple]]):
    for key, asd in trail_dict.items():
        print(key, len(asd), asd)
    return sum(map(len, trail_dict.values()))


if __name__ == "__main__":
    print(solve())
