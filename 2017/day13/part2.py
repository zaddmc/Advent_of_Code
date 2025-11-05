def solve(data):
    data = [tuple(map(int, v.split(": "))) for v in data]

    delay = 0
    while True:
        for dat in data:
            layer, depth = dat

            period = 2 * (depth - 1)
            spot = (delay + layer) % period

            if spot == 0:
                delay += 1
                break
        else:
            return delay


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        print(solve(file.read().strip().splitlines()))
