import sympy


def solve() -> tuple[int, int]:
    get_data()
    print(DATA)
    return (-1, -1)


def get_data():
    global DATA
    with open("../../input/day15.txt", "r") as file:
        DATA = file.read().splitlines()


if __name__ == "__main__":
    print(solve())
