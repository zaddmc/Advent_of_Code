import re
from collections import defaultdict


def solve(data):
    rune = r"^(\w*) (inc|dec) (-?\d*) if (\w*) ([<|>|=|!]*) (-?\d*)$"

    regs = defaultdict(int)
    highest_val = 0

    for dat in data:
        dest, incdec, by, reg, cond, val = re.match(rune, dat).groups()

        res = eval(f"{regs[reg]}" + cond + val)
        if res:
            by = int(by)
            regs[dest] += by if incdec == "inc" else -by
            if regs[dest] > highest_val:
                highest_val = regs[dest]

    return highest_val


if __name__ == "__main__":
    with open("exp.txt", "r") as file:
        DATA = file.read().strip().splitlines()
        assert solve(DATA) == 10

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
        print(solve(DATA))
