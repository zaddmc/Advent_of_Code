def solve(data):
    sum = 0
    for idx, ch in enumerate(data):
        if ch == data[((len(data) // 2) + idx) % len(data)]:
            sum += int(ch)
    return sum


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        DATA = file.read().strip()

    assert solve("1212") == 6
    assert solve("1221") == 0
    assert solve("123425") == 4
    assert solve("123123") == 12
    assert solve("12131415") == 4
    print(solve(DATA))
