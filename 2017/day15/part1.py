def solve(genA, genB):
    genA_factor = 16807
    genB_factor = 48271

    pair_count = 0
    for itt in range(40_000_000):
        genA = genA * genA_factor % 2147483647
        genB = genB * genB_factor % 2147483647

        if bin(genA)[-16:-1] == bin(genB)[-16:-1]:
            pair_count += 1

    print(pair_count)
    return pair_count


if __name__ == "__main__":
    assert solve(65, 8921) == 588

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    genA = int(DATA[0].split()[-1])
    genB = int(DATA[1].split()[-1])

    print(solve(genA, genB))
