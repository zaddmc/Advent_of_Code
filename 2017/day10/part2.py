def solve(data, length):
    values = list(range(length))

    ptr = 0
    skip = 0
    for change in data:
        part = []
        for offset in range(change):
            part.append(values[(ptr + offset) % length])
        part.reverse()
        for offset, val in enumerate(part):
            values[(ptr + offset) % length] = val

        ptr += change + skip
        skip += 1

    return values[0] * values[1]


if __name__ == "__main__":
    # assert solve([3, 4, 1, 5], 5) == 12

    with open("input.txt", "r") as file:
        data = file.read().strip()
    data += ",17,31,73,47,23"
    a = bytes(data, "utf-8") + 
    for v in a:
        print(v, end=",")
    # print(solve(data, 256))
