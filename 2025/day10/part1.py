import re
from heapq import heappop, heappush


def solve(data):
    rune = r"^\[(.*?)\]\s*((?:\([^)]*\)\s*)+) \{([^}]*)\}$"
    total = 0
    for d in data:
        lights, buttons, _ = re.findall(rune, d)[0]
        buttons = tuple(
            tuple(map(int, b.split(",")))
            for b in buttons.replace("(", "").replace(")", "").split()
        )
        total += calc_actions(lights, buttons)
    return total


def calc_actions(lights, buttons):
    not_visited = [(0, "." * len(lights))]

    while not_visited:
        actions, c_lights = heappop(not_visited)

        for but in buttons:
            r_lights = apply_button(c_lights, but)
            if r_lights == lights:
                return actions + 1
            heappush(not_visited, (actions + 1, r_lights))


def apply_button(lights: str, button: tuple[int]):
    for idx in button:
        lights = lights[:idx] + ("#" if lights[idx] == "." else ".") + lights[idx + 1 :]
    return lights


if __name__ == "__main__":
    exp = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
    ]
    assert solve(exp) == 7

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
