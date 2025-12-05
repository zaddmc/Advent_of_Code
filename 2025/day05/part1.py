def solve(ranges, values):
    ranges = [tuple(map(int, r.split("-"))) for r in ranges]
    values = list(map(int, values))

    valid = 0
    for val in values:
        if is_in(ranges, val):
            valid += 1
    return valid


def is_in(ranges, value):
    for ran in ranges:
        if ran[0] <= value <= ran[1]:
            return True


if __name__ == "__main__":
    ranges = ["3-5", "10-14", "16-20", "12-18"]
    values = ["1", "5", "8", "11", "17", "32"]
    assert solve(ranges, values) == 3

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
        split_id = DATA.index("")
        ranges = DATA[:split_id]
        values = DATA[split_id + 1 :]
        print(solve(ranges, values))
