"""No"""

# pylint: disable-msg=C0103

DATA = []
with open("../../input/day4.txt", "r", encoding="utf-8") as source:
    for line in source.readlines():
        DATA.append(line[0:-1])


def check(x, y) -> int:
    """no"""
    succes = 0
    directions = [
        [+1, +1],
        [+1, -1],
        [+1, 0],
        [-1, +1],
        [-1, -1],
        [-1, 0],
        [0, +1],
        [0, -1],
    ]
    for direction in directions:
        for step, target in zip(range(1, 4), "MAS"):
            # Next cordinats and out of bounds check
            nx = x + direction[0] * step
            if nx >= 140 or nx < 0:
                break
            ny = y + direction[1] * step
            if ny >= 140 or ny < 0:
                break

            if target != DATA[nx][ny]:
                break
            succes += 1
    return succes


count = 0
for xdx, line in enumerate(DATA):
    for ydx, letter in enumerate(line):
        if letter == "X":
            count += check(xdx, ydx)
print(count)
