def knot_hash(string: str):
    suffix = b"\x11\x1f\x49\x2f\x17"
    values = list(range(256))
    data = string.encode("utf-8") + suffix

    ptr = 0
    skip = 0
    for _ in range(64):
        for change in data:
            part = []
            for offset in range(change):
                part.append(values[(ptr + offset) % 256])
            part.reverse()
            for offset, val in enumerate(part):
                values[(ptr + offset) % 256] = val

            ptr += change + skip
            skip += 1

    dense = []
    for i in range(0, 256, 16):
        section = map(str, values[i : i + 16])
        dense.append(eval("^".join(section)))

    return dense
