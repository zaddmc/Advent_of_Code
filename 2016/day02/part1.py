def solve(insts):
    keypad = ["123", "456", "789"]
    x = y = 1

    code = ""
    for inst in insts:
        for letter in inst:
            mmin = int((len(keypad) - len(keypad[x])) / 2)
            mmax = int(len(keypad) - ((len(keypad) - len(keypad[x])) / 2)) - 1
            match letter:
                case "U":
                    x -= 1 if x > mmin else 0
                case "D":
                    x += 1 if x < mmax else 0
                case "L":
                    y -= 1 if y > mmin else 0
                case "R":
                    y += 1 if y < mmax else 0
        code += keypad[x][y]

    return int(code)


if __name__ == "__main__":
    test_data = ["ULL", "RRDDD", "LURDL", "UUUUD"]
    assert solve(test_data) == 1985

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
