def solve() -> tuple[int, int]:
    get_data(True)
    trimed_towels = trim_towels()
    p1 = part1(trimed_towels)
    return (p1, -1)


def part1(towels):
    count = len(DESIGNS)
    print(towels)
    for towel in DESIGNS:
        towel_copy = towel
        for ttowel in towels:
            towel_copy = towel_copy.replace(ttowel, "")
        if towel_copy != towel and towel_copy != "":
            print(towel, towel_copy)
            count -= 1
    return count


def trim_towels():
    mod_towels = []
    for towel in TOWELS:
        if len(towel) == 1:
            mod_towels.append(towel)
            continue
        towel_copy = towel
        for ttowel in TOWELS:
            towel_copy = towel_copy.replace(ttowel, "")
        if towel_copy != towel and towel_copy != "":
            mod_towels.append(towel)
    return mod_towels


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
