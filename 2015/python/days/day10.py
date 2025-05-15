def solve() -> tuple[int, int]:
    get_data()
    print(validate("ghijklmn"))
    print(validate("g"))
    return (-1, -1)


def validate(string):
    for char in string:
        if char in "iol":
            return False

    return True


def get_data():
    global DATA
    with open("../../input/day10.txt", "r") as file:
        DATA = file.read().splitlines()


if __name__ == "__main__":
    print(solve())
