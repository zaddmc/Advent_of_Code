import re
from heapq import heappop, heappush

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


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
        m, n = len(joltage), len(buttons)
        A_eq = np.zeros((m, n), dtype=int)
        for idx, but in enumerate(buttons):
            for b in but:
                A_eq[b][idx] = 1
        b_eq = np.array(joltage)
        c = np.array([1 for _ in A_eq[0]])

        bounds = Bounds(lb=np.zeros(4), ub=np.full(4, np.inf))

        eq_constraint = LinearConstraint(A_eq, lb=b_eq, ub=b_eq)
        res = milp(c, integrality=c, constraints=[eq_constraint], bounds=bounds)

        total += pulp.value(prob.objective)
    return total


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
