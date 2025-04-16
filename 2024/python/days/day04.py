def solve() -> tuple[int, int]:
    get_data()
    p1 = part1()
    p2 = part2()
    return (p1, p2)


def get_data():
    global DATA

    DATA = []
    with open("../../input/day04.txt", "r", encoding="utf-8") as source:
        for line in source.readlines():
            DATA.append(line[0:-1])


def part1():
    count = 0
    for xdx, line in enumerate(DATA):
        for ydx, letter in enumerate(line):
            if letter == "X":
                count += check_part1(xdx, ydx)
    return count


def check_part1(x, y) -> int:
    """no"""
    succes = 0
    directions = [
        [+1, +1],
        [+1, -1],
        [+1, 0],
        [-1, +1],
        [-1, -1],
        [-1, 0],
        [0, +1],
        [0, -1],
    ]
    for direction in directions:
        for step, target in zip(range(1, 4), "MAS"):
            # Next cordinats and out of bounds check
            nx = x + direction[0] * step
            if nx >= 140 or nx < 0:
                break
            ny = y + direction[1] * step
            if ny >= 140 or ny < 0:
                break

            if target != DATA[nx][ny]:
                break
            if target == "S":
                succes += 1
    return succes


def part2():
    count = 0
    for xdx, line in enumerate(DATA):
        for ydx, letter in enumerate(line):
            if letter == "A":
                count += check_part2(xdx, ydx)
    return count


def check_part2(x, y) -> int:
    """no"""
    if x >= len(DATA) - 1 or x < 1:
        return 0
    if y >= len(DATA) - 1 or y < 1:
        return 0
    vals = [
        DATA[x + 1][y + 1],  # down-right
        DATA[x + 1][y - 1],  # down-left
        DATA[x - 1][y - 1],  # up-left
        DATA[x - 1][y + 1],  # up-right
    ]
    # Filter out invalid entries
    if "X" in vals or "A" in vals:
        return 0
    # Find Valid postionings
    for rot in range(4):
        if (
            vals[0 + rot] == vals[(1 + rot) % 4]
            and vals[(1 + rot) % 4] != vals[(2 + rot) % 4]
            and vals[(2 + rot) % 4] == vals[(3 + rot) % 4]
        ):
            return 1
    return 0


if __name__ == "__main__":
    print(solve())
