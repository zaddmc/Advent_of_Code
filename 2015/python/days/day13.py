import re
from itertools import pairwise, permutations


def solve() -> tuple[int, int]:
    global PEOPLE
    get_data()

    PEOPLE.remove("Myself")
    p1 = max([evaluate(c) for c in permutations(PEOPLE)])

    PEOPLE.add("Myself")
    p2 = max([evaluate(c) for c in permutations(PEOPLE)])

    return (p1, p2)


def evaluate(configuration):
    happiness = 0
    for per1, per2 in pairwise(configuration):
        happiness += DATA[(per1, per2)]
        happiness += DATA[(per2, per1)]
    else:
        happiness += DATA[(configuration[0], per2)]
        happiness += DATA[(per2, configuration[0])]
    return happiness


def get_data():
    global DATA, PEOPLE
    rune = r"^(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).$"
    with open("../../input/day13.txt", "r") as file:
        DATA = file.read().splitlines()
    DATA = map(lambda s: re.findall(rune, s)[0], DATA)
    DATA = {(p1, p2): int(n) if s == "gain" else -1 * int(n) for p1, s, n, p2 in DATA}

    PEOPLE = set(map(lambda t: t[0], DATA.keys()))
    PEOPLE.add("Myself")
    for perm in permutations(PEOPLE, r=2):
        if perm not in DATA.keys():
            DATA[perm] = 0


if __name__ == "__main__":
    print(solve())
