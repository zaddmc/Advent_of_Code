def solve() -> tuple[int, int]:
    get_data(False)

    values = list(find_all())
    p1 = sum(list(map(lambda lis: lis[-1], values)))
    print(list(find_change(values)))
    return (p1, -1)


def find_change(values):
    for lis in values:
        pre_val = lis[0]
        changes = []
        for val in lis[1:]:
            changes.append(val - pre_val)
            pre_val = val
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
        DATA = [1, 10, 100, 2024]
    else:
        with open("../../input/day22.txt", "r") as file:
            DATA = map(int, file.read().splitlines())


if __name__ == "__main__":
    print(solve())
