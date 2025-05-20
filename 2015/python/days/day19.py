def solve() -> tuple[int, int]:
    get_data(False)
    p1 = len(find_uniques(MOLECULE))
    visited = set()
    visited.add(MOLECULE)
    p2 = deconstruct(0, visited, [MOLECULE], MOLECULE)
    return (p1, p2)


def deconstruct(depth: int, visited: set, last: list, curr: str):
    if curr == "e":
        return depth
    for new in find_uniques(curr):
        if new in visited:
            continue
        visited.add(new)
        last.append(new)
        return deconstruct(depth + 1, visited, last, new)
    last.pop()
    return deconstruct(depth - 1, visited, last, last[-1])


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
