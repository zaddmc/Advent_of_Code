from functools import cache


def solve() -> tuple[int, int]:
    get_data(False)
    p1 = sum([1 for design in DESIGNS if arrange(0, design)])
    p2 = sum(map(count_unique, DESIGNS))
    return (p1, p2)


@cache
def arrange(i, design):
    if i == len(design):
        return True
    for towel in TOWELS:
        if (
            i + len(towel) <= len(design)
            and design[i : i + len(towel)] == towel
            and arrange(i + len(towel), design)
        ):
            return True
    return False


@cache
def count_unique(design: str):
    if not design:
        return 1

    combinations = 0
    for towel in TOWELS:
        if design.startswith(towel):
            combinations += count_unique(design[len(towel) :])
    return combinations


def get_data(test: bool):
    global TOWELS, DESIGNS
    if test:
        TOWELS = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
        DESIGNS = [
            "brwrr",
            "bggr",
            "gbbr",
            "rrbgbr",
            "ubwu",
            "bwurrg",
            "brgr",
            "bbrgwb",
        ]
    else:
        with open("../../input/day19.txt", "r") as file:
            data = file.read().splitlines()
            TOWELS = data[0].split(", ")
            DESIGNS = data[2:]
    TOWELS = set(TOWELS)


if __name__ == "__main__":
    print(solve())
