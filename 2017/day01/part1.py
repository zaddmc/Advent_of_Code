def solve(data):
    sum = 0
    last_char = None
    for idx, ch in enumerate(data):
        if idx == 0:
            last_char = ch
            continue
        if ch == last_char:
            sum += int(ch)
        last_char = ch
    else:
        if ch == data[0]:
            sum += int(ch)
    return sum


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        DATA = file.read().strip()

    assert solve("1122") == 3
    assert solve("1111") == 4
    assert solve("1234") == 0
    assert solve("91212129") == 9
    print(solve(DATA))
