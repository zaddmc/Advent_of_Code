"""No"""

# pylint: disable-msg=C0103

DATA = []
with open("../../input/day4.txt", "r", encoding="utf-8") as source:
    for line in source.readlines():
        DATA.append(line[0:-1])


def check(x, y) -> int:
    """no"""
    if x >= len(DATA) - 1 or x < 1:
        return 0
    if y >= len(DATA) - 1 or y < 1:
        return 0
    vals = [
        DATA[x + 1][y + 1],  # down-right
        DATA[x + 1][y - 1],  # down-left
        DATA[x - 1][y - 1],  # up-left
        DATA[x - 1][y + 1],  # up-right
    ]
    # Filter out invalid entries
    if "X" in vals or "A" in vals:
        return 0
    # Find Valid postionings
    for rot in range(4):
        if (
            vals[0 + rot] == vals[(1 + rot) % 4]
            and vals[(1 + rot) % 4] != vals[(2 + rot) % 4]
            and vals[(2 + rot) % 4] == vals[(3 + rot) % 4]
        ):
            return 1
    return 0


count = 0
for xdx, line in enumerate(DATA):
    for ydx, letter in enumerate(line):
        if letter == "A":
            count += check(xdx, ydx)
print(count)
