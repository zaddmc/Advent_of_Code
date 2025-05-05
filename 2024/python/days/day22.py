def solve() -> tuple[int, int]:
    get_data(False)

    p1 = find_sum()
    return (p1, -1)


def find_sum():
    sum = 0
    for secret in DATA:
        for _ in range(2000):
            secret = next_secret(secret)
        sum += secret
    return sum


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
