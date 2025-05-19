def solve() -> tuple[int, int]:
    get_data(False)
    p1 = len(find_uniques(MOLECULE))
    p2 = make_molecule("e") - 1
    p2 = deconstruct()
    return (p1, p2)


def deconstruct(visited: set, last):
    pass


def make_molecule(curr: str):
    if curr == MOLECULE:
        return 1
    if len(curr) > len(MOLECULE):
        return 0
    for nm in find_uniques(curr):
        res = make_molecule(nm)
        if res:
            return res + 1


def find_uniques(curr):
    uniques = set()
    for re in REPLACEMENTS:
        re_key, re_val = re.split(" ")

        prev_index = 0
        for _ in range(curr.count(re_key)):
            index = curr.find(re_key, prev_index)
            uniques.add(curr[:index] + curr[index:].replace(re_key, re_val, 1))

            prev_index = index + 1
    return uniques


def get_data(test: bool):
    global REPLACEMENTS, MOLECULE
    if test:
        with open("../../input/day19.exp.txt", "r") as file:
            data = file.read().splitlines()
            REPLACEMENTS = list(map(lambda s: s.replace("=> ", ""), data[:-2]))
            MOLECULE = data[-1]

    else:
        with open("../../input/day19.txt", "r") as file:
            data = file.read().splitlines()
            REPLACEMENTS = list(map(lambda s: s.replace("=> ", ""), data[:-2]))
            MOLECULE = data[-1]


if __name__ == "__main__":
    print(solve())
