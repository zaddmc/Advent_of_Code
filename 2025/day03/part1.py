def solve(data):
    value = 0

    for line in data:
        first = find_val(line, True)
        second = find_val(line[line.find(first) + 1 :], False)

        if first and second:
            value += int(first + second)
    return value


def find_val(line: str, isfirst: bool):
    for t in range(9, -1, -1):
        t = str(t)
        if t in line:
            if isfirst and line.count(t) == 1 and line[-1] == t:
                continue
            return t
    return -1


if __name__ == "__main__":
    test = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
    assert solve(test) == 357

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
