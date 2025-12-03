def solve(data):
    value = 0
    for line in data:
        value += int(find_max(line, 12))
    return value


def find_max(bank: str, length: int):
    if length == 0:
        return ""
    next_digit: str = max(bank[: len(bank) - length + 1])
    next_digit_pos: int = bank.find(next_digit)
    return next_digit + find_max(bank[next_digit_pos + 1 :], length - 1)
    return next_digit + max_joltage(bank[next_digit_pos + 1 :], length - 1)


if __name__ == "__main__":
    test = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
    assert solve(test) == 3121910778619

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
