import numpy as np


def solve() -> tuple[int, int]:
    get_data()
    p1 = interpret()
    p2 = interpret_elvish()
    return (p1, p2)


def interpret():
    grid = np.zeros((1000, 1000))
    for action, frm, _, to in INSTRUCTIONS:
        x0, y0 = map(int, frm.split(","))
        x1, y1 = map(int, to.split(","))

        match action:
            case "on":
                grid[x0 : x1 + 1, y0 : y1 + 1] = 1
            case "off":
                grid[x0 : x1 + 1, y0 : y1 + 1] = 0
            case "toggle":
                grid[x0 : x1 + 1, y0 : y1 + 1] = 1 - grid[x0 : x1 + 1, y0 : y1 + 1]

    return int(grid.sum())


def interpret_elvish():
    grid = np.zeros((1000, 1000))
    for action, frm, _, to in INSTRUCTIONS:
        x0, y0 = map(int, frm.split(","))
        x1, y1 = map(int, to.split(","))

        match action:
            case "on":
                grid[x0 : x1 + 1, y0 : y1 + 1] += 1
            case "off":
                grid[x0 : x1 + 1, y0 : y1 + 1] = np.maximum(
                    0, grid[x0 : x1 + 1, y0 : y1 + 1] - 1
                )
            case "toggle":
                grid[x0 : x1 + 1, y0 : y1 + 1] += 2

    for row in grid:
        for col in row:
            if col < 0:
                print(col)
    return int(grid.sum())


def get_data():
    global INSTRUCTIONS
    with open("../../input/day06.txt", "r") as file:
        INSTRUCTIONS = file.read().splitlines()
    INSTRUCTIONS = list(map(lambda s: s.replace("turn ", "").split(" "), INSTRUCTIONS))


if __name__ == "__main__":
    print(solve())
