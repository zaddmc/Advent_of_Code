def solve(DATA):
    data = gen(DATA)
    length = 0
    char_mult = 1
    consume = 0

    for char in data:
        if consume:
            consume -= 1
            length += char_mult
            continue
        if char == "(":
            buf = ""
            flag = False
            for schar in data:
                if schar == ")":
                    char_mult = int(buf)
                    break
                if schar == "x":
                    consume = int(buf)
                    buf = ""
                    flag = True
                    continue
                buf += schar
            continue
        length += 1

    return length


def gen(string):
    for char in string:
        yield char


if __name__ == "__main__":
    assert solve("ADVENT") == 6
    assert solve("A(1x5)BC") == 7
    assert solve("(3x3)XYZ") == 9
    assert solve("(6x1)(1x3)A") == 6
    assert solve("X(8x2)(3x3)ABCY") == 18

    with open("input.txt", "r") as file:
        DATA = file.read().strip()
    print(solve(DATA))
