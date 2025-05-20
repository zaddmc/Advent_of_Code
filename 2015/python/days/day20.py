from functools import reduce


def solve() -> tuple[int, int]:
    get_data()
    p1 = brute_force_simple()
    p2 = brute_force_broad()
    return (p1, p2)


def brute_force_broad():
    house = 1
    while True:
        lefactors = factors(house)
        presents = sum(11 * p for p in lefactors if house // p <= 50)
        if presents >= DATA:
            return house
        house += 1


def brute_force_simple():
    house = 1
    while True:
        presents = sum(10 * p for p in factors(house))
        if presents >= DATA:
            return house
        house += 1


def factors(n):
    return set(
        reduce(
            list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)
        )
    )


def get_data():
    global DATA
    with open("../../input/day20.txt", "r") as file:
        DATA = int(file.read().strip())


if __name__ == "__main__":
    print(solve())
