def solve() -> tuple[int, int]:
    get_data()
    p1 = sum([len(s) - len(eval(s)) for s in DATA])
    p2 = sum([len(repr(s).replace('"', '\\"')) - len(s) for s in DATA])
    return (p1, p2)


def get_data():
    global DATA
    with open("../../input/day08.txt", "r") as file:
        DATA = file.read().splitlines()


if __name__ == "__main__":
    print(solve())
