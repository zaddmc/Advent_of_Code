def get_diff(row: str):
    cols = list(map(int, row.split()))
    return max(cols) - min(cols)


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        DATA = file.read().strip().splitlines()

    checksum = 0
    for l in DATA:
        checksum += get_diff(l)
    print(checksum)
