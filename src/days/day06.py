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
print(GUARD_POS)
print(GUARD_DIRECTION)
