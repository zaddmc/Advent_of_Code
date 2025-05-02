from queue import Queue


def solve() -> tuple[int, int]:
    get_data(False)
    p1 = run()
    swap_wires()
    print(bin(p1))
    return (p1, -1)


def swap_wires():
    x_bits = ""
    y_bits = ""
    for key, val in map(lambda e: e.split(), INITIAL):
        if key[0] == "x":
            x_bits += val
        elif key[0] == "y":
            y_bits += val
    x_bits = x_bits[::-1]
    print("x:", x_bits)
    y_bits = y_bits[::-1]
    print("y:", y_bits)

    bit_goal = int(x_bits, 2) + int(y_bits, 2)
    print(bin(bit_goal))

    for lkey, opt, rkey, dest in map(
        lambda e: e.split(), map(lambda e: e.replace("-> ", ""), OPERATIONS)
    ):
        if lkey[0] == "x" and rkey[0] == "y" and opt == "AND":
            # print(lkey, opt, rkey, dest)
            pass


def run():
    memory = {}
    for key, val in [initial.split(": ") for initial in INITIAL]:
        memory[key] = int(val)

    operations = Queue()
    for oper in OPERATIONS:
        operations.put(oper.replace("-> ", ""))

    operators = {
        "OR": lambda x, y: x | y,
        "AND": lambda x, y: x & y,
        "XOR": lambda x, y: x ^ y,
    }

    while not operations.empty():
        lkey, opt, rkey, dest = operations.get().split()

        if lkey in memory.keys() and rkey in memory.keys():
            memory[dest] = operators[opt](memory[lkey], memory[rkey])
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
