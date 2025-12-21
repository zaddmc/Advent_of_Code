import re


def solve(instructions: list[str], a_start: int) -> int:
    memory = {"a": a_start, "b": 0}
    ip = 0  # Instruction Pointer
    while True:
        if ip >= len(instructions):
            return memory["b"]
        inst = instructions[ip]

        match inst[:3]:
            case "hlf":
                memory[inst[4]] //= 2
            case "tpl":
                memory[inst[4]] *= 3
            case "inc":
                memory[inst[4]] += 1
            case "jmp":
                res = re.findall(r"(.)(\d+)", inst)[0]
                ip += int(res[1]) if res[0] == "+" else -1 * int(res[1])
                continue
            case "jie":
                if memory[inst[4]] % 2 == 0:
                    res = re.findall(r"(.)(\d+)", inst)[0]
                    ip += int(res[1]) if res[0] == "+" else -1 * int(res[1])
                    continue
            case "jio":
                if memory[inst[4]] == 1:
                    res = re.findall(r"(.)(\d+)", inst)[0]
                    ip += int(res[1]) if res[0] == "+" else -1 * int(res[1])
                    continue
            case x:
                print("Left:", x)
                return
        ip += 1


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().splitlines()

    p1 = solve(DATA, 0)
    p2 = solve(DATA, 1)
    print(p1, p2)
