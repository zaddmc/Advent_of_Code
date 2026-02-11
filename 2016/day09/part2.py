def solve(string: str):
    if "(" not in string:
        return len(string)
    length = 0
    while "(" in string:
        dist = string.find("(")
        length += dist
        string = string[dist:]

        dist = string.find(")")
        chars, mult = string[1:dist].split("x")
        string = string[dist + 1 :]
        length += solve(string[: int(chars)] * int(mult))
        string = string[int(chars) :]
    length += len(string)
    return length


if __name__ == "__main__":
    assert solve("(3x3)XYZ") == 9
    assert solve("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920
    assert solve("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445

    with open("input.txt", "r") as file:
        DATA = file.read().strip()
    print(solve(DATA))
