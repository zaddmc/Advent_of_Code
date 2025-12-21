import re


def solve() -> tuple[int, int]:
    get_data()
    computer()
    return (-1, -1)


def computer():
    memory = {"a": 0, "b": 0}
    ip = 0  # Instruction Pointer
    while True:
        inst = INSTRUCTIONS[ip]

        if inst.startswith("hlf"):
            memory[inst[4]] //= 2
        elif inst.startswith("tpl"):
            memory[inst[4]] *= 3
        elif inst.startswith("inc"):
            memory[inst[4]] += 1
        elif inst.startswith("jmp"):
            res = re.findall(r"(.)(\d+)", inst)[0]
            ip += int(res[1]) if res[0] == "+" else -1 * int(res[1])
            print(ip)
            continue
        elif inst.startswith("jie"):
            if memory[inst[4]] % 2 == 0:
                res = re.findall(r"(.)(\d+)", inst)[0]
                ip += int(res[1]) if res[0] == "+" else -1 * int(res[1])
                print(ip)
                continue
        elif inst.startswith("jio"):
            if memory[inst[4]] == 1:
                res = re.findall(r"(.)(\d+)", inst)[0]
                ip += int(res[1]) if res[0] == "+" else -1 * int(res[1])
                continue
        else:
            return

        ip += 1


def get_data():
    global INSTRUCTIONS
    with open("../../input/day23.txt", "r") as file:
        INSTRUCTIONS = file.read().splitlines()


if __name__ == "__main__":
    print(solve())
