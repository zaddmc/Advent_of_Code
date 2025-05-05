def solve() -> tuple[int, int]:
    get_data(False)

    values = list(find_all())
    p1 = sum(list(map(lambda lis: lis[-1], values)))
    changes = list(find_change(values))
    # p2 = sum([result_series(change, [-2, 1, -1, 3]) for change in changes])

    p2 = max(list(brute_force(changes)))
    return (p1, p2)


def brute_force(changes: list[list]):
    low, high = -3, 4
    for x in range(low, high):
        for y in range(low, high):
            for z in range(low, high):
                for w in range(low, high):
                    yield sum(
                        [result_series(change, [x, y, z, w]) for change in changes]
                    )


def result_series(serie: list[int], target: list[int]):
    previous = serie[:4]
    banana = sum(previous)
    for val in serie[4:]:
        previous.pop(0)
        banana += val
        previous.append(val)

        if previous == target:
            return banana
    return 0


def find_change(values):
    for lis in values:
        pre_val = lis[0] % 10
        changes = [pre_val]
        for val in lis[1:]:
            changes.append(val % 10 - pre_val)
            pre_val = val % 10
        yield changes


def find_all():
    for secret in DATA:
        secrets = [secret]
        for _ in range(2000):
            secrets.append(next_secret(secrets[-1]))
        yield secrets


def next_secret(secret: int) -> int:
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret


def mix(num1: int, num2: int) -> int:
    return num1 ^ num2


def prune(num: int) -> int:
    return num % 16777216


def get_data(test: bool):
    global DATA
    if test:
        DATA = [1, 2, 3, 2024]
    else:
        with open("../../input/day22.txt", "r") as file:
            DATA = map(int, file.read().splitlines())


if __name__ == "__main__":
    print(solve())
