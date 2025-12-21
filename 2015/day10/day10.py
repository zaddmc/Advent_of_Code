def solve() -> tuple[int, int]:
    get_data()
    string = DATA
    for _ in range(40):
        string = expand(string)
    p1 = len(string)
    for _ in range(10):
        string = expand(string)
    p2 = len(string)
    return (p1, p2)


def expand(string):
    previous_char = string[0]
    count = 1
    new_string = ""
    for new_char in string[1:]:
        if new_char == previous_char:
            count += 1
        else:
            new_string += str(count) + previous_char
            previous_char = new_char
            count = 1
    else:
        new_string += str(count) + previous_char

    return new_string


def get_data():
    global DATA
    with open("../../input/day10.txt", "r") as file:
        DATA = file.read().strip()


if __name__ == "__main__":
    print(solve())
