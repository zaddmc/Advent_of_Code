def part2(replacements, molecule: str):
    vals = set()
    for key, _ in replacements:
        vals.add(key)

    tokens = 0
    for val in vals:
        tokens += molecule.count(val)

    tokens -= molecule.count("Y")

    return tokens - 1


def part1(replacements, molecule: str):
    unique = set()
    for key, val in replacements:
        index = 0
        for _ in range(molecule.count(key)):
            index = molecule.find(key, index)
            unique.add(molecule[:index] + molecule[index:].replace(key, val, 1))
            index += 1
    return len(unique)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        *replacements, _, molecule = file.read().strip().splitlines()
    replacements = [(k, v) for k, v in map(lambda s: s.split(" => "), replacements)]

    p1 = part1(replacements, molecule)
    p2 = part2(replacements, molecule)
    print(p1, p2)
