def solve(data):
    value = 0

    for line in data:
        line = [int(i) for i in line]
        value += find_val(line)

    return value


def find_val(arr):
    return 1


if __name__ == "__main__":
    test = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
    assert solve(test) == 3121910778619

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
