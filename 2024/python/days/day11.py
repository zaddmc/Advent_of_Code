from collections import Counter


def solve() -> tuple[int, int]:
    get_data()

    stones = Counter(map(int, DATA.split()))
    stones = blink_n(stones, 25)
    b_25 = count_stones(stones)

    stones = blink_n(stones, 50)
    b_75 = count_stones(stones)

    return (b_25, b_75)


def get_data(test_data: bool = False) -> str:
    global DATA
    if test_data:
        DATA = "125 17"
    else:
        with open("../../input/day11.txt", "r") as file:
            DATA = file.read().strip()
    return DATA


def blink(stones: Counter):
    new_stones = Counter()
    for val, qty in stones.items():
        if val == 0:
            new_stones[1] += qty
            continue

        elm_str = str(val)
        elm_len = len(elm_str)
        if elm_len % 2 == 0:
            new_stones[int(elm_str[: elm_len // 2])] += qty
            new_stones[int(elm_str[elm_len // 2 :])] += qty
            continue
        new_stones[val * 2024] += qty

    return new_stones


def blink_n(stones: Counter, n: int) -> Counter:
    for _ in range(n):
        stones = blink(stones)
    return stones


def count_stones(stones: Counter) -> int:
    return sum(stones.values())


if __name__ == "__main__":
    print(solve())
