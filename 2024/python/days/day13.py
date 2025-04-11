def solve() -> tuple[int, int]:
    get_data()
    tokens = 0
    for _ in range(len(DATA) // 4 + 1):
        tokens += claw_machine()
    return (tokens, -1)


def claw_machine() -> int:
    segment = next_segment()
    claw_A = disect(segment[0])
    claw_B = disect(segment[1])
    goal = disect(segment[2])

    return brute_force(claw_A, claw_B, goal)


def brute_force(claw_A, claw_B, goal) -> int:
    possible = []
    for a in range(100):
        for b in range(100):
            if tup_add(tup_mul(claw_A, a), tup_mul(claw_B, b)) == goal:
                possible.append(a * 3 + b)
    if len(possible) == 0:
        return 0
    possible.sort()
    return possible[0]


def disect(seg: str) -> tuple[int, int]:
    lhs = seg[seg.index("X") + 2 : seg.index(",")]
    rhs = seg[seg.index("Y") + 2 :]
    return (int(lhs), int(rhs))


def tup_mul(tup: tuple[int, int], mul: int) -> tuple[int, int]:
    return (tup[0] * mul, tup[1] * mul)


def tup_add(tup1: tuple[int, int], tup2: tuple[int, int]) -> tuple[int, int]:
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])


segment_progress = -1


def next_segment():
    global segment_progress
    segment_progress += 1
    return DATA[segment_progress * 4 : segment_progress * 4 + 3]


def get_data():
    global DATA
    with open("../../input/day13.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    return DATA


if __name__ == "__main__":
    print(solve())
