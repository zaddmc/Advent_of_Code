def solve(moves):
    moves = moves.split(",")

    cancel_opposite(moves)
    reduce_between(moves)

    return len(moves)


def reduce_between(moves):
    items = ["n", "ne", "se", "s", "sw", "nw"]
    for offset in range(6):
        left = items[offset]
        center = items[(offset + 1) % 6]
        right = items[(offset + 2) % 6]

        common_count = min(moves.count(left), moves.count(right))
        for _ in range(common_count):
            moves.remove(left)
            moves.remove(right)
            moves.append(center)


def cancel_opposite(moves):
    for can in [("n", "s"), ("ne", "sw"), ("nw", "se")]:
        common_count = min(moves.count(can[0]), moves.count(can[1]))

        for _ in range(common_count):
            moves.remove(can[0])
            moves.remove(can[1])


if __name__ == "__main__":
    assert solve("ne,ne,ne") == 3
    assert solve("ne,ne,sw,sw") == 0
    assert solve("ne,ne,s,s") == 2
    assert solve("se,sw,se,sw,sw") == 3

    with open("input.txt", "r") as file:
        DATA = file.read().strip()
    print(solve(DATA))
