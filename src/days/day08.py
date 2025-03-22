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


def find_antinode(val1: tuple[int, int], val2: tuple[int, int]) -> int:
    new_antinodes: int = 0
    delta = get_delta(val1, val2)

    new_antinodes += do_calc(val1, delta, sub_tuple)
    new_antinodes += do_calc(val2, delta, add_tuple)
    return new_antinodes


def do_calc(val, delta, operator):
    if in_bounds(operator(val, delta)):
        fish = operator(val, delta)
        if DATA[fish[0]][fish[1]] != "#":
            DATA[fish[0]] = (
                DATA[fish[0]][: fish[1]] + "#" + DATA[fish[0]][fish[1] + 1 :]
            )
            return 1
    return 0


def add_tuple(val1: tuple[int, int], val2: tuple[int, int]) -> tuple[int, int]:
    return (val1[0] + val2[0], val1[1] + val2[1])


def sub_tuple(val1: tuple[int, int], val2: tuple[int, int]) -> tuple[int, int]:
    return (val1[0] - val2[0], val1[1] - val2[1])


def get_delta(val1: tuple[int, int], val2: tuple[int, int]) -> tuple[int, int]:
    return (val2[0] - val1[0], val2[1] - val1[1])


def in_bounds(val: tuple[int, int]) -> bool:
    return 0 <= val[0] < SIZE and 0 <= val[1] < SIZE


def pr():
    for line in DATA:
        print(line)
    print(f"{p1=}")


# Iterate thru antenna frequencies and determine
p1 = 0
for freq, vals in antenna_dict.items():
    for val in vals:
        for other in vals[vals.index(val, 0, 1000) + 1 :]:
            p1 += find_antinode(val, other)
print(f"{p1=}")
