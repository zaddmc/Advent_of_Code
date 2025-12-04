def solve(data):
    rolls = 0
    for idx, row in enumerate(data):
        for idy, item in enumerate(row):
            if item != "@":
                continue
            free_space = [
                data[x][y]
                for x, y in [
                    (idx + 1, idy),
                    (idx - 1, idy),
                    (idx, idy + 1),
                    (idx, idy - 1),
                    (idx + 1, idy + 1),
                    (idx + 1, idy - 1),
                    (idx - 1, idy + 1),
                    (idx - 1, idy - 1),
                ]
                if 0 <= x < len(data) and 0 <= y < len(data[0])
            ].count("@")
            if free_space < 4:
                rolls += 1
    return rolls


if __name__ == "__main__":
    item = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]
    assert solve(item) == 13

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
