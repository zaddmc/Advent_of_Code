"""No"""

MAP = []
GUARD_POS = (-1, -1)
GUARD_DIRECTION = ""
with open("../../input/day6.txt", "r", encoding="utf-8") as map_file:
    for idline, line in enumerate(map_file.readlines()):
        MAP.append(line[:-1])

        if GUARD_POS != (-1, -1):
            continue
        for idletter, letter in enumerate(line):
            if letter in "^>v<":
                GUARD_POS = (idline, idletter)
                GUARD_DIRECTION = letter

max_index = len(MAP)
DISTINCT_TILES = 0


def move_guard():
    """no"""
    global GUARD_DIRECTION, DISTINCT_TILES, MAP
    line, letter = GUARD_POS
    match GUARD_DIRECTION:
        case "^":
            line -= 1
        case ">":
            letter += 1
        case "v":
            line += 1
        case "<":
            letter -= 1
        case _:
            raise Exception

    if line > max_index or letter > max_index or line < 0 or letter < 0:
        DISTINCT_TILES += 1  # Otherwise its of by 1
        return (-69, -69)

    if MAP[line][letter] in ".X":
        if MAP[line][letter] == ".":
            DISTINCT_TILES += 1
            MAP[line] = MAP[line][:letter] + "X" + MAP[line][letter + 1 :]

        return (line, letter)

    # print("changed direction")
    posible_directions = "^>v<"
    GUARD_DIRECTION = posible_directions[
        (posible_directions.index(GUARD_DIRECTION) + 1) % 4
    ]
    return GUARD_POS


while GUARD_POS != (-69, -69):
    GUARD_POS = move_guard()
    # for line in MAP:
    #    print(line)
    # print(f"Pos: {GUARD_POS} Direction: {GUARD_DIRECTION}")
    # print(DISTINCT_TILES)
print(DISTINCT_TILES)
