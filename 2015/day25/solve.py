import re


def solve(start, coords):
    row, column = coords
    mult = 252533
    remain = 33554393

    exponent = int((row + column - 2) * (row + column - 1) / 2 + column - 1)
    return (pow(mult, exponent, remain) * start) % remain


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().strip()
    coords = map(int, re.findall(r"\d+", DATA))
    print(solve(20151125, coords))
