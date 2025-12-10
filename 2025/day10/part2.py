import re
from heapq import heappop, heappush

from scipy.optimize import linprog


def solve(data):
    rune = r"^\[(.*?)\]\s*((?:\([^)]*\)\s*)+) \{([^}]*)\}$"
    total = 0
    for d in data:
        buttons, joltage = re.findall(rune, d)[0][1:]
        joltage = tuple(map(int, joltage.split(",")))

        buttons = tuple(
            tuple(map(int, b.split(",")))
            for b in buttons.replace("(", "").replace(")", "").split()
        )
        new_buttons = [[0 for _ in buttons] for _ in joltage]
        for i in range(6):
            for j in range(4):
                new_buttons[j][i] = 1 if j in buttons[i] else 0

        c = [1 for _ in buttons]
        A_eq = new_buttons
        b_eq = joltage
        print(c, A_eq, b_eq, sep="\n")
        print(linprog(c, A_ub=A_eq, b_ub=b_eq))
    print(total)
    return total


def calc_actions(joltage: tuple[int], buttons: tuple[int]):
    not_visited = [(0, joltage)]

    while not_visited:
        actions, c_joltage = heappop(not_visited)

        for but in buttons:
            r_joltage = apply_button(c_joltage, but)
            if sum(joltage) == 0:
                return actions + 1
            if is_valid(r_joltage):
                heappush(not_visited, (actions + 1, r_joltage))


def is_valid(joltage: tuple[int]):
    for j in joltage:
        if j < 0:
            return
    return True


def apply_button(joltage: tuple[int], button: tuple[int]):
    joltage = list(joltage)
    for idx in button:
        joltage[idx] -= 1
    return tuple(joltage)


if __name__ == "__main__":
    exp = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
    ]
    assert solve(exp) == 33

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
