from collections import defaultdict


def solve(codes):
    columns = [defaultdict(int) for _ in codes[0]]

    for code in codes:
        for idx, letter in enumerate(code):
            columns[idx][letter] += 1

    msg = ""
    for column in columns:
        min_key = None
        min_value = 1000
        for key, value in column.items():
            if value < min_value:
                min_key = key
                min_value = value
        msg += min_key
    return msg


if __name__ == "__main__":
    # fmt: off
    test_data = ["eedadn", "drvtee", "eandsr", "raavrd", "atevrs", "tsrnev", "sdttsa", "rasrtv", "nssdts", "ntnada", "svetve", "tesnvt", "vntsnd", "vrdear", "dvrsen", "enarar"]
    # fmt: on
    assert solve(test_data) == "advent"

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
