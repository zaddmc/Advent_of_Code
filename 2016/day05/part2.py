from hashlib import md5


def solve(doorID: str):
    password = [""] * 8

    found = 0
    idx = 0
    while True:
        string = doorID + str(idx)
        idx += 1

        md5hash = md5(string.encode()).hexdigest()
        if not (md5hash[:5] == "0" * 5):
            continue

        index = md5hash[5]
        if not index.isdigit():
            continue

        index = int(index)
        if not index < 8:
            continue
        if password[index] != "":
            continue

        password[index] += md5hash[6]

        found += 1
        if found == 8:
            return "".join(password)


if __name__ == "__main__":
    # assert solve("abc") == "05ace8e3"

    with open("input.txt", "r") as file:
        DATA = file.read().strip()
    print(solve(DATA))
