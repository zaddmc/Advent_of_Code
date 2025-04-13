def solve() -> tuple[int, int]:
    get_data(True)
    generate_numeral_dict()

    print(numeric(DATA[0]))
    return (-1, -1)


def numeric(code: str) -> str:
    mcode = "A" + code
    replacement = ""
    for idx in range(len(code)):
        replacement += numeral(mcode[idx], mcode[idx + 1])
    return replacement


def numeral(start: str, end: str) -> str:
    return "a"


def generate_numeral(start: str, end: str) -> str:
    start_pos = get_index(start)
    end_pos = get_index(end)

    res_vec = (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
    result = ""

    return "a"


def generate_numeral_dict() -> dict:
    chars = "A0123456789"
    ndict = {}  # numeral dict
    for start in chars:
        for end in chars:
            res = generate_numeral(start, end)
            ndict[start + end] = res
            print(res)


def get_index(char: str) -> tuple[int, int]:
    layout = ["789", "456", "123", " 0A"]
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
