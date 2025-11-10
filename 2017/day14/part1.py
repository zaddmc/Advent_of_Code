from knot_hash import knot_hash


def solve(data):
    memory = []
    for val in range(128):
        memory.append(
            "".join(
                [
                    f"{bin(val).removeprefix("0b"):>08}"
                    for val in knot_hash(data + "-" + str(val))
                ]
            )
        )
    return sum([s.count("1") for s in memory])


if __name__ == "__main__":
    assert solve("flqrgnkx") == 8108

    with open("input.txt", "r") as file:
        print(solve(file.read().strip()))
