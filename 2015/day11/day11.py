def solve() -> tuple[int, int]:
    get_data()
    string = DATA
    p1 = None
    p2 = None
    while True:
        string = increment(string)
        if validate(string):
            if not p1:
                p1 = string
                continue
            if not p2:
                p2 = string
                break

    return (p1, p2)


def increment(string):
    increment_next = True
    new_string = ""
    for byte in string.encode()[::-1]:
        if increment_next:
            byte += 1
            increment_next = False

        if byte + 1 > 123:
            increment_next = True
            new_string += "a"
            continue

        new_string += chr(byte)
    else:
        if increment_next:
            new_string += "a"
    return new_string[::-1]


def validate(string):
    prev_2 = ""
    prev_3 = ""

    seq_2 = set()
    seq_3 = False
    for char in string:
        if char in "iol":
            return False
        prev_2 = prev_2 + char if len(prev_2) < 2 else prev_2[1:] + char
        prev_3 = prev_3 + char if len(prev_3) < 3 else prev_3[1:] + char

        prev_2_byt = prev_2.encode()
        if len(prev_2) >= 2 and prev_2_byt[0] == prev_2_byt[1]:
            seq_2.add(prev_2_byt)

        prev_3_byt = prev_3.encode()
        if (
            len(prev_3) >= 3
            and prev_3_byt[0] + 1 == prev_3_byt[1]
            and prev_3_byt[1] + 1 == prev_3_byt[2]
        ):
            seq_3 = True
    return seq_3 and len(seq_2) >= 2


def get_data():
    global DATA
    with open("../../input/day11.txt", "r") as file:
        DATA = file.read().strip()


if __name__ == "__main__":
    print(solve())
