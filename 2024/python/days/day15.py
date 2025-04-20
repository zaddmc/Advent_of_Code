def solve() -> tuple[int, int]:
    get_data(False)
    begin()
    p1 = gps_sum()
    return (p1, -1)


def begin():
    global POS
    find_start_pos()

    for move in MOVES:
        if not check_move(move, POS):
            continue
        do_move(move, POS, ".")
        POS = tup_add(POS, DIRECTION_DICT[move])
        continue
        pr_map()
        print(move)
        input()


def do_move(dir, pos, new_char):
    global MAP
    next_char = map_tup(pos)
    MAP[pos[1]][pos[0]] = new_char

    new_pos = tup_add(pos, DIRECTION_DICT[dir])

    match map_tup(new_pos):
        case "O":
            do_move(dir, new_pos, next_char)
        case "#":
            raise Exception("Should not have been found")
        case ".":
            MAP[new_pos[1]][new_pos[0]] = next_char
        case "@":
            raise Exception("Should not find oneself")
        case _:
            raise Exception("Life is so jover")


def check_move(dir, pos):
    pos = tup_add(pos, DIRECTION_DICT[dir])

    match map_tup(pos):
        case "O":
            return check_move(dir, pos)
        case "#":
            return False
        case ".":
            return True
        case "@":
            raise Exception("Should not find oneself")
        case _:
            raise Exception("Life is so jover")


def gps_sum():
    def gps_cords():
        for idx, line in enumerate(MAP):
            for idy, char in enumerate(line):
                if char == "O":
                    yield idy + idx * 100

    return sum(gps_cords())


DIRECTION_DICT = {"<": (-1, 0), "^": (0, -1), ">": (1, 0), "v": (0, 1)}


def tup_add(tup1: tuple[int, int], tup2: tuple[int, int]) -> tuple[int, int]:
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])


def map_tup(tup=0):
    if tup == 0:
        return MAP[POS[1]][POS[0]]
    if isinstance(tup, str) and tup in "<v^>":
        pos = tup_add(POS, DIRECTION_DICT[tup])
        return map_tup(pos)
    return MAP[tup[1]][tup[0]]


def pr_map():
    for line in MAP:
        for char in line:
            print(char, end="")
        print()


def find_start_pos() -> tuple[int, int]:
    global POS
    for idx, line in enumerate(MAP):
        for idy, char in enumerate(line):
            if char == "@":
                POS = (idx, idy)


def get_data(test: bool):
    global MAP, MOVES
    if test:
        MAP = [
            "##########",
            "#..O..O.O#",
            "#......O.#",
            "#.OO..O.O#",
            "#..O@..O.#",
            "#O#..O...#",
            "#O..O..O.#",
            "#.OO.O.OO#",
            "#....O...#",
            "##########",
        ]
        MOVES = (
            "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^"
            "vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v"
            "><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<"
            "<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^"
            "^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><"
            "^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^"
            ">^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^"
            "<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>"
            "^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>"
            "v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"
        )
    else:
        with open("../../input/day15.txt", "r") as file:
            map, moves = file.read().strip().split("\n\n")
            MAP = map.splitlines()
            MOVES = moves.replace("\n", "")
    MAP = [list(line) for line in MAP]


if __name__ == "__main__":
    print(solve())
