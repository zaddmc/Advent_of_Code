def solve() -> tuple[int, int]:
    global DATA, SIZE
    DATA = get_data()
    SIZE = len(DATA)
    trails = {}
    trail_score = 0
    for idx, line in enumerate(DATA):
        for idy, height in enumerate(line):
            if height == "0":
                trails[(idx, idy)] = []
                trail_score += find_trail(idx, idy, "0", trails[(idx, idy)])
    return (trail_score, -1)


def get_data():
    return open("../../input/day10.txt", "r").read().strip().split()


def find_trail(idx: int, idy: int, next_val: str, trail_list: list):

    if not 0 < idx < SIZE - 1 or not 0 < idy < SIZE - 1:
        return

    if DATA[idx][idy] == "9":
        if (idx, idy) not in trail_list:
            trail_list.append((idx, idy))

    if DATA[idx][idy] != next_val:
        # input(f"{idx=}, {idy=} {next_val=}   {DATA[idx][idy]}")
        return

    check = "0123456789"  # The next value to find
    new_next_val = check[check.index(next_val, 0, 10) + 1]
    find_trail(idx + 1, idy, new_next_val, trail_list)
    find_trail(idx - 1, idy, new_next_val, trail_list)
    find_trail(idx, idy + 1, new_next_val, trail_list)
    find_trail(idx, idy - 1, new_next_val, trail_list)
    return


if __name__ == "__main__":
    print(solve())
