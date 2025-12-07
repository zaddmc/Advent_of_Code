from heapq import heappop, heappush


def solve(mp):
    start = (0, mp[0].index("S"))
    not_visited = [start]
    splits = 0

    while not_visited:
        cur_row, cur_col = heappop(not_visited)
        cur_row += 1

        if cur_row == len(mp):  # At end
            continue

        match mp[cur_row][cur_col]:
            case ".":
                if (cur_row, cur_col) not in not_visited:
                    heappush(not_visited, (cur_row, cur_col))
            case "^":
                splits += 1
                if (cur_row, cur_col + 1) not in not_visited:
                    heappush(not_visited, (cur_row, cur_col + 1))
                if (cur_row, cur_col - 1) not in not_visited:
                    heappush(not_visited, (cur_row, cur_col - 1))
            case _:
                print("wha")
    return splits


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
    assert solve(exp) == 21

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
