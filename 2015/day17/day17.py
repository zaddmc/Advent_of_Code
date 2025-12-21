def solve() -> tuple[int, int]:
    get_data()
    data = list(find_combinations([], DATA))
    p1 = len(data)
    min_len = len(min(data, key=len))
    p2 = sum([1 if len(d) == min_len else 0 for d in data])
    return (p1, p2)


def find_combinations(curr, remain):
    if sum(curr) == 150:
        yield curr
    elif sum(curr) < 150:
        new_remain = remain.copy()
        for re in remain:
            new_remain.remove(re)
            new_curr = curr.copy()
            new_curr.append(re)
            yield from find_combinations(new_curr, new_remain)


def get_data():
    global DATA
    with open("../../input/day17.txt", "r") as file:
        DATA = sorted(map(int, file.read().splitlines()), reverse=True)


if __name__ == "__main__":
    print(solve())
