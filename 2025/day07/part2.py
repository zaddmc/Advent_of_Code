def solve(mp):
    start = (0, mp[0].index("S"))  # Format is row, col
    counter = {start: 1}
    result = 0

    while counter:
        cur_row, cur_col = min(counter.keys())
        amount = counter.pop((cur_row, cur_col))
        cur_row += 1
        tup = (cur_row, cur_col)

        if cur_row == len(mp):  # At end
            result += amount
            continue

        match mp[cur_row][cur_col]:
            case ".":
                if tup in counter.keys():
                    counter[tup] += amount
                else:
                    counter[tup] = amount
            case "^":
                for offset in [1, -1]:
                    if (cur_row, cur_col + offset) in counter.keys():
                        counter[(cur_row, cur_col + offset)] += amount
                    else:
                        counter[(cur_row, cur_col + offset)] = amount

            case _:
                print("wha")
    return result


if __name__ == "__main__":
    exp = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]
    assert solve(exp) == 40

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
