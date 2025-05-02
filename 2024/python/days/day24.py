from queue import Queue


def solve() -> tuple[int, int]:
    get_data(False)
    p1 = run()
    return (p1, -1)


def run():
    memory = {}
    for key, val in [initial.split(": ") for initial in INITIAL]:
        memory[key] = int(val)

    operations = Queue()
    for oper in OPERATIONS:
        operations.put(oper.replace("-> ", ""))

    while not operations.empty():
        lkey, opt, rkey, dest = operations.get().split()

        if lkey in memory.keys() and rkey in memory.keys():
            match opt:
                case "AND":
                    memory[dest] = memory[lkey] and memory[rkey]
                case "OR":
                    memory[dest] = memory[lkey] or memory[rkey]
                case "XOR":
                    memory[dest] = memory[lkey] ^ memory[rkey]
                case _:
                    raise Exception("Unkown Operator")
            continue

        operations.put(f"{lkey} {opt} {rkey} {dest}")

    bits = ""
    for key in sorted(memory.keys(), reverse=True):
        bits += str(memory[key]) if key[0] == "z" else ""
    return int(bits, 2)


def get_data(test: bool):
    global INITIAL, OPERATIONS
    if test:
        with open("../../input/day24exp.txt", "r") as file:
            init, operations = file.read().split("\n\n")
            INITIAL = init.splitlines()
            OPERATIONS = operations.splitlines()
    else:
        with open("../../input/day24.txt", "r") as file:
            init, operations = file.read().split("\n\n")
            INITIAL = init.splitlines()
            OPERATIONS = operations.splitlines()


if __name__ == "__main__":
    print(solve())
