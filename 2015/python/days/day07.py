from collections import deque


def solve() -> tuple[int, int]:
    get_data()
    p1 = emulate(None)
    p2 = emulate(p1)
    return (p1, p2)


def emulate(override):
    insts = deque(INSTRUCTIONS)
    memory = {}
    while insts:
        instruction = insts.popleft()
        parts = instruction.split(" ")

        if "AND" in parts:
            if parts[0] in memory.keys() and parts[2] in memory.keys():
                memory[parts[-1]] = memory[parts[0]] & memory[parts[2]]
            elif parts[0].isdigit() and parts[2] in memory.keys():
                memory[parts[-1]] = int(parts[0]) & memory[parts[2]]
            else:
                insts.append(instruction)
            continue

        if "OR" in parts:
            if parts[0] in memory.keys() and parts[2] in memory.keys():
                memory[parts[-1]] = memory[parts[0]] | memory[parts[2]]
            else:
                insts.append(instruction)
            continue

        if "NOT" in parts:
            if parts[1] in memory.keys():
                memory[parts[-1]] = ~memory[parts[1]]
            else:
                insts.append(instruction)
            continue

        if "LSHIFT" in parts:
            if parts[0] in memory.keys():
                memory[parts[-1]] = memory[parts[0]] << int(parts[2])
            else:
                insts.append(instruction)
            continue

        if "RSHIFT" in parts:
            if parts[0] in memory.keys():
                memory[parts[-1]] = memory[parts[0]] >> int(parts[2])
            else:
                insts.append(instruction)
            continue

        if parts[0].isdigit():
            if override and parts[-1] == "b":
                memory[parts[-1]] = override
            else:
                memory[parts[-1]] = int(parts[0])
            continue

        if parts[0] in memory.keys():
            return memory[parts[0]]

        insts.append(instruction)

    print(memory)


def get_data():
    global INSTRUCTIONS
    with open("../../input/day07.txt", "r") as file:
        INSTRUCTIONS = file.read().splitlines()


if __name__ == "__main__":
    print(solve())
