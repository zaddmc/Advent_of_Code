def solve() -> tuple[int, int]:
    get_data()
    p1 = DATA.count("(") - DATA.count(")")
    p2 = first_negative()
    return (p1, p2)


def first_negative():
    pointer = 0
    for i, char in enumerate(DATA):
        if pointer < 0:
            return i
        pointer += 1 if char == "(" else -1


def get_data():
    global DATA
    with open("../../input/day01.txt", "r") as file:
        DATA = file.read()


if __name__ == "__main__":
    print(solve())
