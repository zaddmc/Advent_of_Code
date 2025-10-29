def solve(string: str):
    memory = []
    working = list(map(int, string.split()))

    while tuple(working) not in memory:
        memory.append(tuple(working))
        redistribute(working)

    return len(memory) - memory.index(tuple(working))


def redistribute(working: list[int]):
    max_val = max(working)
    max_idx = working.index(max_val)
    working[max_idx] = 0

    for idx in range(max_val):
        working[(max_idx + idx + 1) % len(working)] += 1


if __name__ == "__main__":
    assert solve("0 2 7 0") == 4

    with open("./input.txt", "r") as file:
        data = file.read().strip()
    print(solve(data))
