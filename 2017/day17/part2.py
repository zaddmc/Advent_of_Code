"""I was given a revelation, that 0 is always at index 0"""


def solve(mdist):
    cur_pos = 0
    value_after_zero = 0
    for itt in range(1, 50_000_000):
        cur_pos = (cur_pos + mdist) % itt

        if cur_pos == 0:
            value_after_zero = itt

        cur_pos += 1
    return value_after_zero


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = int(file.read().strip())
    print(solve(DATA))
