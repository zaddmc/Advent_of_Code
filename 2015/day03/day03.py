def solve() -> tuple[int, int]:
    get_data()
    p1 = follow()
    return (p1, -1)


def follow():
    row = col = 0
    rrow = rcol = 0
    houses = set()
    houses.add((0, 0))
    for i, move in enumerate(DATA):
        if i % 2 == 0:
            row, col = {
                "<": (row - 1, col),
                ">": (row + 1, col),
                "^": (row, col - 1),
                "v": (row, col + 1),
            }[move]
            houses.add((row, col))
        else:
            rrow, rcol = {
                "<": (rrow - 1, rcol),
                ">": (rrow + 1, rcol),
                "^": (rrow, rcol - 1),
                "v": (rrow, rcol + 1),
            }[move]
            houses.add((rrow, rcol))
    return len(houses)


def get_data():
    global DATA
    with open("../../input/day03.txt", "r") as file:
        DATA = file.read()


if __name__ == "__main__":
    print(solve())
