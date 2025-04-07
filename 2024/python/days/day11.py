def solve() -> tuple[int, int]:
    get_data()

    stones = map(int, DATA.split())
    for _ in range(25):
        stones = blink(stones)

    return (len(stones), -1)


def get_data(test_data: bool = False) -> str:
    global DATA
    if test_data:
        DATA = "125 17"
    else:
        with open("../../input/day11.txt", "r") as file:
            DATA = file.read().strip()
    return DATA


def blink(stones: list[int]):
    new_stones: list[int] = []
    for elm in stones:
        if elm == 0:
            new_stones.append(1)
            continue

        elm_str = str(elm)
        elm_len = len(elm_str)
        if elm_len % 2 == 0:
            new_stones.append(int(elm_str[: elm_len // 2]))
            new_stones.append(int(elm_str[elm_len // 2 :]))
            continue

        new_stones.append(elm * 2024)

    return new_stones


if __name__ == "__main__":
    print(solve())
