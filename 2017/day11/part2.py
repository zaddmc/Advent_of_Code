"""
Solution inspired by
https://en.wikipedia.org/wiki/Hexagonal_Efficient_Coordinate_System#/media/File:HECS_Nearest_Neighbors.png
"""


def solve(moves):
    moves = moves.split(",")

    north = 0  # C
    neast = 0  # R
    seast = 0  # A

    max_len = 0

    for move in moves:
        match move:
            case "n":
                north += 1
            case "s":
                north += -1
            case "ne":
                neast += seast
                north += seast
                seast = 1 - seast
            case "sw":
                north -= 1 - seast
                neast -= 1 - seast
                seast = 1 - seast
            case "se":
                north -= 1 - seast
                neast += seast
                seast = 1 - seast
            case "nw":
                north += seast
                neast -= 1 - seast
                seast = 1 - seast
            case _:
                print("Explode", _)

        cur_len = abs(north) + abs(neast) + abs(seast)
        if cur_len > max_len:
            max_len = cur_len

    return max_len


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().strip()
    print(solve(DATA))
