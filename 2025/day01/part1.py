def solve(intstructions: list[str]):
    pointing = 50
    zeros = 0

    for inst in intstructions:
        if inst[0] == "L":
            pointing -= int(inst[1:])
        else:
            pointing += int(inst[1:])

        pointing %= 100
        if pointing == 0:
            zeros += 1
    return zeros


if __name__ == "__main__":
    assert (
        solve(["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]) == 3
    )

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
