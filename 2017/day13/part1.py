def solve(data):
    severity = 0

    for dat in data:
        layer, depth = map(int, dat.split(": "))

        period = 2 * (depth - 1)
        spot = layer % period

        if spot == 0:
            severity += layer * depth
    return severity


if __name__ == "__main__":
    with open("example.txt", "r") as file:
        assert solve(file.read().strip().splitlines()) == 24

    with open("input.txt", "r") as file:
        print(solve(file.read().strip().splitlines()))
