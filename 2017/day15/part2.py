def solve(genA, genB):
    genA_factor = 16807
    genB_factor = 48271

    Agen = gen(genA_factor, genA, 4)
    Bgen = gen(genB_factor, genB, 8)

    pair_count = 0
    for itt in range(5_000_000):
        a_val = next(Agen)
        b_val = next(Bgen)

        if a_val & 0xFFFF == b_val & 0xFFFF:
            pair_count += 1

    return pair_count


def gen(factor: int, start_val: int, mult: int):
    val = start_val
    while True:
        val = val * factor % 2147483647
        if val % mult == 0:
            yield val


if __name__ == "__main__":
    assert solve(65, 8921) == 309

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    genA = int(DATA[0].split()[-1])
    genB = int(DATA[1].split()[-1])

    print(solve(genA, genB))
