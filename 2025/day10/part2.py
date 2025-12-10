import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


def solve(data):
    total = 0
    for d in data:
        buttons, joltage = d.split("] (")[1].split(") {")
        joltage = np.array(tuple(map(int, joltage[:-1].split(","))))
        buttons = tuple(
            tuple(map(int, b.split(",")))
            for b in buttons.replace("(", "").replace(")", "").split()
        )
        m, n = len(joltage), len(buttons)
        A_eq = np.zeros((m, n), dtype=int)
        for idx, but in enumerate(buttons):
            for b in but:
                A_eq[b][idx] = 1

        c = np.full(n, 1)
        bounds = Bounds(lb=np.zeros(n), ub=np.full(n, np.inf))
        eq_constraint = LinearConstraint(A_eq, lb=joltage, ub=joltage)

        res = milp(c, integrality=c, constraints=[eq_constraint], bounds=bounds)
        total += res.fun
    return int(total)


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
