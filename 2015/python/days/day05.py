from itertools import pairwise


def solve() -> tuple[int, int]:
    get_data()
    p1 = sum([1 for s in DATA if is_valid(s)])
    p2 = sum([1 for s in DATA if is_valid_v2(s)])
    return (p1, p2)


def is_valid(s):
    if sum([s.count(v) for v in ["a", "e", "i", "o", "u"]]) < 3:
        return False

    for val in pairwise(s):
        if val[0] == val[1]:
            break
    else:
        return False

    for nono in ["ab", "cd", "pq", "xy"]:
        if nono in s:
            return False

    return True


def is_valid_v2(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            break
    else:
        return False

    for val in pairwise(s):
        if s.count("".join(val)) >= 2:
            break
    else:
        return False

    return True


def get_data():
    global DATA
    with open("../../input/day05.txt", "r") as file:
        DATA = file.read().splitlines()


if __name__ == "__main__":
    print(solve())
