def solve() -> tuple[int, int]:
    get_data()
    p1 = interpret()
    return (p1, -1)


def interpret():
    actions = {
        "toggle": lambda b: not b,
        "on": lambda _: True,
        "off": lambda _: False,
    }
    for action, frm, _, to in map(lambda s: s.split(" "), INSTRUCTIONS):
        for line in range(*map(int, frm.split(","))):
            for val in range(*map(int, to.split(","))):
                GRID[line][val] = actions[action](GRID[line][val])

    count = 0
    for line in GRID:
        for val in line:
            count += val
    return count


def get_data():
    global INSTRUCTIONS, GRID
    with open("../../input/day06.txt", "r") as file:
        INSTRUCTIONS = file.read().splitlines()
    INSTRUCTIONS = map(lambda s: s.replace("turn ", ""), INSTRUCTIONS)
    GRID = [[False for _ in range(1000)] for _ in range(1000)]


if __name__ == "__main__":
    print(solve())
