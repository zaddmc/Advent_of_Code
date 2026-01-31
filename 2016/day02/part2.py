def solve(insts):
    keypad = ["xx1xx", "x234x", "56789", "xABCx", "xxDxx"]
    x = 2
    y = 0
    dictionary = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    code = ""
    for inst in insts:
        for letter in inst:
            xc, yc = dictionary[letter]
            x += xc
            y += yc
            if not (0 <= x < 5 and 0 <= y < 5 and keypad[x][y] != "x"):
                x -= xc
                y -= yc

        code += keypad[x][y]
    return code


if __name__ == "__main__":
    test_data = ["ULL", "RRDDD", "LURDL", "UUUUD"]
    assert solve(test_data) == "5DB3"

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
