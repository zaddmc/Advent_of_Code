from functools import cache


def solve() -> tuple[int, int]:
    global ndict
    get_data(True)
    ndict = {}
    generate_dict(False)
    generate_dict(True)

    return (part1(), -1)


def part1():
    length = 0
    goal = [
        "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
        "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A",
        "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
        "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A",
        "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
    ]
    for code, goa in zip(DATA, goal):
        print(code)
        step = convert(code)
        print(step)

        step = convert(step)
        print(step)
        step = convert(step)

        length += len(step) * int(code[:-1])
        print("mine", step)
        print("goal", goa)
        print()
    return length


def convert(code: str) -> str:
    mcode = "A" + code
    replacement = ""
    for idx in range(len(code)):
        replacement += ndict[mcode[idx] + mcode[idx + 1]]
    return replacement


def translate(start: str, end: str, isnum: bool) -> str:
    start_pos = get_index(start, isnum)
    end_pos = get_index(end, isnum)

    vertical = end_pos[0] - start_pos[0]
    horizontal = end_pos[1] - start_pos[1]
    result = ""

    if isnum and start_pos[0] == 0:
        result += tran_hor(horizontal)
        result += tran_ver(vertical)
    elif isnum and start_pos[1] == 3:
        result += tran_ver(vertical)
        result += tran_hor(horizontal)
    elif start == "<":
        result += tran_hor(horizontal)
        result += tran_ver(vertical)
    elif end == "<":
        result += tran_ver(vertical)
        result += tran_hor(horizontal)
    else:
        result += tran_hor(horizontal)
        result += tran_ver(vertical)

    result += "A"
    return result


def tran_ver(val):
    if val < 0:
        return "^" * (val * -1)
    else:
        return "v" * val


def tran_hor(val):
    if val < 0:
        return "<" * (val * -1)
    else:
        return ">" * val


def generate_dict(isnum: bool) -> dict:
    global ndict
    chars = "A0123456789" if isnum else "A^<v>"
    for start in chars:
        for end in chars:
            res = translate(start, end, isnum)
            ndict[start + end] = res
    return ndict


@cache
def get_index(char: str, isnum: bool) -> tuple[int, int]:
    layout = ["789", "456", "123", " 0A"] if isnum else [" ^A", "<v>"]
    for idx, row in enumerate(layout):
        idy = row.find(char, 0, 3)
        if idy != -1:
            return (idx, idy)
    raise Exception("Char not found")


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
