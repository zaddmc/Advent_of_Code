def solve(data, length):

    values = list(range(length))

    ptr = 0
    skip = 0
    for _ in range(64):
        for change in data:
            part = []
            for offset in range(change):
                part.append(values[(ptr + offset) % length])
            part.reverse()
            for offset, val in enumerate(part):
                values[(ptr + offset) % length] = val

            ptr += change + skip
            skip += 1

    return values


if __name__ == "__main__":
    suffix = b"\x11\x1f\x49\x2f\x17"

    assert solve(b"3,4,1,5" + suffix, 5) == 12

    with open("input.txt", "r") as file:
        data = file.read().strip()
    start = "1,2,3"
    suffix = b"\x11\x1f\x49\x2f\x17"
    asd = start.encode("utf-8") + suffix
    for b in asd:
        print(b, end=", ")

    # print(solve(data, 256))
