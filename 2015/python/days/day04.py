import hashlib


def solve() -> tuple[int, int]:
    get_data()
    p1 = find_hash(5)
    p2 = find_hash(6)
    return (p1, p2)


def find_hash(zeroes: int):
    num = 0
    while True:
        result = hashlib.md5(f"{DATA}{str(num)}".encode())
        if result.hexdigest()[:zeroes] == "0" * zeroes:
            return num
        num += 1


def get_data():
    global DATA
    with open("../../input/day04.txt", "r") as file:
        DATA = file.read().strip()


if __name__ == "__main__":
    print(solve())
