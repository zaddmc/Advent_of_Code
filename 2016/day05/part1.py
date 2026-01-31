from hashlib import md5


def solve(doorID: str):
    password = ""

    idx = 0
    while True:
        string = doorID + str(idx)
        md5hash = md5(string.encode()).hexdigest()
        if md5hash[:5] == "0" * 5:
            password += md5hash[5]
            if len(password) == 8:
                return password
        idx += 1


if __name__ == "__main__":
    # assert solve("abc") == "18f47a30"

    with open("input.txt", "r") as file:
        DATA = file.read().strip()
    print(solve(DATA))
