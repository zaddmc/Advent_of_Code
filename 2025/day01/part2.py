def solve(intstructions: list[str]):
    pointing = 50
    zeros = 0

    for inst in intstructions:
        num = int(inst[1:])
        pointing += num if inst[0] == "R" else -num

        zeros += abs(pointing // 100)
        pointing %= 100
        # crossing, pointing = divmod(pointing, 100)
        # zeros += abs(crossing)
    return zeros


def shit(intstructions: list[str]):
    pointing = 50
    zeros = 0

    for inst in intstructions:
        num = int(inst[1:])
        for _ in range(num):
            pointing += 1 if inst[0] == "R" else -1
            pointing %= 100
            if pointing == 0:
                zeros += 1
    return zeros


if __name__ == "__main__":
    assert (
        shit(["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]) == 6
    )

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(shit(DATA))
