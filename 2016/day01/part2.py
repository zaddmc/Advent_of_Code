def solve(insts):
    dir = 0
    x = y = 0
    path = set()

    for inst in insts:
        if inst[0] == "R":
            dir += 1
        else:
            dir += -1
        dir %= 4
        change = [(0, 1), (-1, 0), (0, -1), (1, 0)][dir]

        val = int(inst[1:])
        for i in range(val):
            nx, ny = change
            x += nx
            y += ny

            if (x, y) in path:
                return abs(x) + abs(y)

            path.add((x, y))


if __name__ == "__main__":
    assert solve(["R8", "R4", "R4", "R8"]) == 4

    with open("input.txt", "r") as file:
        DATA = file.read().strip().split(", ")
    print(solve(DATA))
