def solve(data, length=256):
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

    dense = []
    for i in range(0, length, 16):
        section = map(str, values[i : i + 16])
        dense.append(eval("^".join(section)))

    return int_arr_to_hex_str(dense)


def int_arr_to_hex_str(data):
    string = ""
    for val in data:
        temp = hex(val).removeprefix("0x")
        string += "0" + temp if len(temp) == 1 else temp
    return string


if __name__ == "__main__":
    suffix = b"\x11\x1f\x49\x2f\x17"

    assert solve(b"" + suffix) == "a2582a3a0e66e6e86e3812dcb672a272"
    assert solve(b"AoC 2017" + suffix) == "33efeb34ea91902bb2f59c9920caa6cd"
    assert solve(b"1,2,3" + suffix) == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert solve(b"1,2,4" + suffix) == "63960835bcdc130f0b66d7ff4f6a5a8e"

    with open("input.txt", "rb") as file:
        data = file.read().strip()
    data += suffix

    print(solve(data))
