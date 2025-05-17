def solve() -> tuple[int, int]:
    get_data()
    p1 = max(brute_force(4))
    p2 = max(brute_force(5))

    return (p1, p2)


def brute_force(cal):
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c
                # print(list(evaluate((a, b, c, d))))
                yield evaluate((a, b, c, d), cal)


def evaluate(ratios, c):
    result = 1
    for i, values in enumerate(DATA[:c]):
        res = sum([ratio * val for val, ratio in zip(values, ratios)])
        if i == 4:
            return result if res == 500 else 0
        result *= res if res > 0 else 1
    return result


def get_data():
    global DATA
    with open("../../input/day15.txt", "r") as file:
        data = file.read().splitlines()
    DATA = [[int(v.split(" ")[i].strip(",")) for v in data] for i in range(2, 11, 2)]


if __name__ == "__main__":
    print(solve())
