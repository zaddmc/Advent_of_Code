def solve() -> tuple[int, int]:
    get_data(False)
    p1 = check()
    return (p1, -1)


def check():
    count = 0
    for lock in LOCKS:
        for key in KEYS:
            if max(combine_lists(lock, key)) <= 5:
                count += 1
    return count


def get_data(test: bool):
    global KEYS, LOCKS
    KEYS, LOCKS = [], []
    if test:
        with open("../../input/day25exp.txt", "r") as file:
            data = map(lambda s: s.splitlines(), file.read().split("\n\n"))
    else:
        with open("../../input/day25.txt", "r") as file:
            data = map(lambda s: s.splitlines(), file.read().split("\n\n"))

    for val in data:
        if val[0] == "#####":
            KEYS.append(count_col(val[1:-1]))
        else:
            LOCKS.append(count_col(val[1:-1]))


def combine_lists(list1, list2):
    for val1, val2 in zip(list1, list2):
        yield val1 + val2


def count_col(thing):
    count = [0 for _ in range(5)]
    for row in thing:
        for idx, char in enumerate(row):
            if char == "#":
                count[idx] += 1
    return count


if __name__ == "__main__":
    print(solve())
