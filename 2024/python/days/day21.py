from functools import cache
from itertools import pairwise


def solve() -> tuple[int, int]:
    get_data(False)
    p1 = start(2)
    p2 = start(25)
    return (p1, p2)


NUMERIC = "789" "456" "123" " 0A"
ARROWS = " ^A" "<v>"


def start(steps: int) -> int:
    return sum(cost(NUMERIC, code, steps + 1) * int(code[:-1]) for code in DATA)


@cache
def cost(keypad: str, path: str, steps: int) -> int:
    return sum(step_cost(keypad, a, b, steps) for a, b in pairwise("A" + path))


@cache
def step_cost(keypad: str, start: str, end: str, steps: int) -> int:
    return (
        min(cost(ARROWS, path, steps - 1) for path in calc_path(keypad, start, end))
        if steps
        else 1
    )


def calc_path(keypad: str, start: str, end: str):
    y1, x1 = divmod(keypad.index(start), 3)
    y2, x2 = divmod(keypad.index(end), 3)
    hor = "<>"[x2 > x1] * abs(x2 - x1)
    ver = "^v"[y2 > y1] * abs(y2 - y1)
    for path in {hor + ver, ver + hor}:
        if " " not in walk(keypad, x1, y1, path):
            yield path + "A"


def walk(keypad, x, y, path):
    i = y * 3 + x
    for direction in path:
        i += (-1, 1, -3, 3)["<>^v".index(direction)]
        yield keypad[i]


def get_data(test: bool = False):
    global DATA
    if test:
        DATA = ["029A", "980A", "179A", "456A", "379A"]
    else:
        with open("../../input/day21.txt", "r") as file:
            DATA = file.read().strip().splitlines()
    return DATA


if __name__ == "__main__":
    print(solve())
