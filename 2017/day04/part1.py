def validate(passphrase: str):
    sections = passphrase.split(" ")
    return len(sections) == len(set(sections))


def solve(data):
    valid = 0
    for string in data:
        valid += int(validate(string))
    return valid


if __name__ == "__main__":
    assert solve(["aa bb cc dd ee"]) == 1
    assert solve(["aa bb cc dd aa"]) == 0
    assert solve(["aa bb cc dd aaa"]) == 1

    with open("./input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
