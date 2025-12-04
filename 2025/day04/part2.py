def solve(data):
    rolls_removed = 0
    my_map = data.copy()

    while True:
        my_map, removed = run(my_map)
        rolls_removed += removed
        if removed == 0:
            break
    return rolls_removed


def run(mp: list[str]):
    new_map = mp.copy()
    rolls_removed = 0
    for idx, row in enumerate(mp):
        for idy, item in enumerate(row):
            if item != "@":
                continue
            free_space = [
                mp[x][y]
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
                if 0 <= x < len(mp) and 0 <= y < len(mp[0])
            ].count("@")
            if free_space < 4:
                new_map[idx] = new_map[idx][:idy] + "." + new_map[idx][idy + 1 :]
                rolls_removed += 1
    return new_map, rolls_removed


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
    assert solve(item) == 43

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
