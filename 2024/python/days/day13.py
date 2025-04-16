def solve() -> tuple[int, int]:
    get_data()
    p1 = sum(claw_machine(segment, False) for segment in get_segments())
    p2 = sum(claw_machine(segment, True) for segment in get_segments())
    return (p1, p2)


def claw_machine(segment, ispart2: bool) -> int:
    claw_A = disect(segment[0])
    claw_B = disect(segment[1])
    goal = disect(segment[2])

    if ispart2:
        goal = (goal[0] + 10000000000000, goal[1] + 10000000000000)

    # return min(modding(claw_A, claw_B, goal), default=0)
    return min(brute_force(claw_A, claw_B, goal), default=0)


def brute_force(claw_A, claw_B, goal) -> int:
    for a in range(100):
        for b in range(100):
            if tup_add(tup_mul(claw_A, a), tup_mul(claw_B, b)) == goal:
                yield a * 3 + b


def modding(claw_A, claw_B, goal) -> int:
    yield 0


def disect(seg: str) -> tuple[int, int]:
    lhs = seg[seg.index("X") + 2 : seg.index(",")]
    rhs = seg[seg.index("Y") + 2 :]
    return (int(lhs), int(rhs))


def tup_mul(tup: tuple[int, int], mul: int) -> tuple[int, int]:
    return (tup[0] * mul, tup[1] * mul)


def tup_add(tup1: tuple[int, int], tup2: tuple[int, int]) -> tuple[int, int]:
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])


def get_segments():
    for prog in range(len(DATA) // 4 + 1):
        yield DATA[prog * 4 : prog * 4 + 3]


def get_data():
    global DATA
    with open("../../input/day13.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    return DATA


if __name__ == "__main__":
    print(solve())
