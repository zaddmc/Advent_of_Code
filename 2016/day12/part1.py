from collections import defaultdict


def solve(instructions: str):
    registers = defaultdict(int)

    ip = 0
    while True:
        if not (0 <= ip < len(instructions)):
            break

        cmd, *args = instructions[ip].split()
        match cmd:
            case "cpy":
                if args[0].lstrip("-").isdigit():
                    arg1 = int(args[0])
                else:
                    arg1 = registers[args[0]]
                registers[args[1]] = arg1

            case "inc":
                registers[args[0]] += 1
            case "dec":
                registers[args[0]] -= 1
            case "jnz":
                if args[0].lstrip("-").isdigit():
                    arg1 = int(args[0])
                else:
                    arg1 = registers[args[0]]
                if arg1 != 0:
                    ip += int(args[1])
                    continue
            case _:
                print("Unknown inst:", inst)
        ip += 1
    return registers["a"]


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
