def is_divisble(val1, val2):
    if val1 / val2 == val1 // val2:
        return val1 // val2
    if val2 / val1 == val2 // val1:
        return val2 // val1
    return 0


def get_diff(row: str):
    cols = sorted(list(map(int, row.split())))

    sum = 0
    for idx in range(len(cols)):
        for idy in range(len(cols) - 1, idx, -1):
            sum += is_divisble(cols[idx], cols[idy])
    return sum


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        DATA = file.read().strip().splitlines()

    checksum = 0
    for l in DATA:
        checksum += get_diff(l)
    print(checksum)
