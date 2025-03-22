DATA: list[str] = []
with open("../../input/day8.txt", "r") as file:
    DATA = file.read().splitlines()

SIZE: int = len(DATA)  # max size for both col length and height

antenna_dict: dict[str, list[tuple]] = {}


def add_to_dict(letter: str, idx: int, idy: int) -> None:
    global antenna_dict
    try:
        antenna_dict[letter].append((idx, idy))
    except KeyError:
        antenna_dict[letter] = [(idx, idy)]


# Find Antennas
for idx, line in enumerate(DATA):
    for idy, letter in enumerate(line):
        if letter == ".":
            continue
        add_to_dict(letter, idx, idy)


def find_antinode(val1: tuple[int, int], val2: tuple[int, int], mul):
    delta = get_delta(val1, val2)

    do_calc(val1, delta, sub_tuple, mul)
    do_calc(val2, delta, add_tuple, mul)


def do_calc(val, delta, operator, mul):
    node = operator(val, delta)
    while in_bounds(node):
        if in_bounds(node):
            if DATA[node[0]][node[1]] != "#":
                DATA[node[0]] = (
                    DATA[node[0]][: node[1]] + "#" + DATA[node[0]][node[1] + 1 :]
                )
        if not mul:
            break
        node = operator(node, delta)


def add_tuple(val1: tuple[int, int], val2: tuple[int, int]) -> tuple[int, int]:
    return (val1[0] + val2[0], val1[1] + val2[1])


def sub_tuple(val1: tuple[int, int], val2: tuple[int, int]) -> tuple[int, int]:
    return (val1[0] - val2[0], val1[1] - val2[1])


def get_delta(val1: tuple[int, int], val2: tuple[int, int]) -> tuple[int, int]:
    return (val2[0] - val1[0], val2[1] - val1[1])


def in_bounds(val: tuple[int, int]) -> bool:
    return 0 <= val[0] < SIZE and 0 <= val[1] < SIZE


def pr(val):
    for line in DATA:
        print(line)
    print(f"{val=}")


def go_through(mul: bool):
    for freq, vals in antenna_dict.items():
        for val in vals:
            for other in vals[vals.index(val, 0, 1000) + 1 :]:
                find_antinode(val, other, mul)


def count_dathing(mul: bool):
    count = 0
    for line in DATA:
        for letter in line:
            if mul:
                if letter != ".":
                    count += 1
            else:
                if letter == "#":
                    count += 1
    return count


# Iterate thru antenna frequencies and determine
go_through(False)
p1 = count_dathing(False)
print(f"{p1=}")

go_through(True)
p2 = count_dathing(True)
print(f"{p2=}")
