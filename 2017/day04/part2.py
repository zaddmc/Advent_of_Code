def validate(passphrase: str):
    sections = tuple(map(lambda l: "".join(sorted(l)), passphrase.split(" ")))
    return len(sections) == len(set(sections))


def solve(data):
    valid = 0
    for string in data:
        valid += int(validate(string))
    return valid


if __name__ == "__main__":
    assert solve(["abcde fghij"]) == 1

    with open("./input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
