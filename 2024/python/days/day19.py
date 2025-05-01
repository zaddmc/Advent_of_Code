def solve() -> tuple[int, int]:
    get_data(False)
    p1 = sum([1 for design in DESIGNS if arrange(0, design)])
    # regex_rune = regex()
    # p1 = sum([1 for design in DESIGNS if re.search(regex_rune, design)])
    return (p1, -1)


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


def regex():
    pattern = r"^(?:"
    for towel in TOWELS:
        pattern += "(" + towel + ")|"
    pattern = pattern[:-1]
    pattern += ")+$"
    return pattern


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


if __name__ == "__main__":
    print(solve())
