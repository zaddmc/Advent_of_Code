def solve() -> tuple[int, int]:
    get_data()
    p1, p2 = calc()
    return (p1, p2)


def calc():
    paper = 0
    ribbon = 0
    for length, width, height in DATA:
        length, width, height = int(length), int(width), int(height)
        paper += 2 * length * width + 2 * width * height + 2 * height * length
        paper += min([length * width, width * height, height * length])

        ribbon += min(
            2 * length + 2 * width, 2 * width + 2 * height, 2 * height + 2 * length
        )

        ribbon += length * width * height
    return paper, ribbon


def get_data():
    global DATA
    with open("../../input/day02.txt", "r") as file:
        DATA = list(map(lambda e: e.split("x"), file.read().splitlines()))


if __name__ == "__main__":
    print(solve())
