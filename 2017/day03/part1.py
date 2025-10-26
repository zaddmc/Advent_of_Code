from spiral import gen_spiral


def solve(target):
    matrix = gen_spiral(int(target**0.5) + 1)
    x1, y1 = find_val(matrix, target)
    x2, y2 = find_val(matrix, 1)

    return abs(x1 - x2) + abs(y1 - y2)


def find_val(matrix, target):
    for idx, row in enumerate(matrix):
        for idy, val in enumerate(row):
            if val == target:
                return idx, idy


if __name__ == "__main__":
    assert solve(12) == 3
    assert solve(23) == 2
    assert solve(1024) == 31

    with open("./input.txt", "r") as file:
        TARGET = int(file.read().strip())
    print(solve(TARGET))
