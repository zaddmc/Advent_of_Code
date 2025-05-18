def solve() -> tuple[int, int]:
    get_data(False)
    frame = DATA
    for _ in range(SIZE):
        frame = step(frame, False)
    p1 = count_lights(frame)

    frame = alter_frame(DATA)
    for _ in range(SIZE):
        frame = step(frame, True)
    p2 = count_lights(frame)
    return (p1, p2)


def count_lights(frame):
    count = 0
    for row in frame:
        for cell in row:
            if cell == "#":
                count += 1
    return count


def alter_frame(frame):
    new_frame = frame.copy()
    new_frame[0] = "#" + new_frame[0][1:-1] + "#"
    new_frame[-1] = "#" + new_frame[-1][1:-1] + "#"
    return new_frame


def step(old_frame, alter):
    new_frame = [""] * SIZE
    for ir, row in enumerate(old_frame):
        for ic, cell in enumerate(row):
            if cell == "#":
                new_frame[ir] += (
                    "#" if find_neighbors(old_frame, ir, ic) in [2, 3] else "."
                )
            else:
                new_frame[ir] += "#" if find_neighbors(old_frame, ir, ic) == 3 else "."
    if alter:
        new_frame = alter_frame(new_frame)
    return new_frame


def find_neighbors(frame, row, col):
    count = 0
    for x, y in [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col + 1),
        (row + 1, col + 1),
        (row + 1, col),
        (row + 1, col - 1),
        (row, col - 1),
    ]:
        if 0 <= x < SIZE and 0 <= y < SIZE:
            if frame[x][y] == "#":
                count += 1
    return count


def pr_frame(frame):
    for row in frame:
        print(row)
    print()


def get_data(test: bool):
    global DATA, SIZE
    if test:
        with open("../../input/day18.exp.txt", "r") as file:
            DATA = file.read().splitlines()
        SIZE = 6
    else:
        with open("../../input/day18.txt", "r") as file:
            DATA = file.read().splitlines()
        SIZE = 100


if __name__ == "__main__":
    print(solve())
