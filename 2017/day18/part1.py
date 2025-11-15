from collections import defaultdict


def solve(data):
    ip = 0
    regs = defaultdict(int)

    last_sound = 0

    while True:
        try:
            inst = data[ip].split()
        except:
            break
        ip += 1

        match inst[0]:
            case "snd":
                last_sound = get_val(regs, inst[1])
            case "set":
                regs[inst[1]] = get_val(regs, inst[2])
            case "add":
                regs[inst[1]] += get_val(regs, inst[2])
            case "mul":
                regs[inst[1]] *= get_val(regs, inst[2])
            case "mod":
                regs[inst[1]] %= get_val(regs, inst[2])
            case "rcv":
                if get_val(regs, inst[1]) > 0:
                    return last_sound
            case "jgz":
                if get_val(regs, inst[1]) > 0:
                    ip -= 1  # To counter the start
                    ip += get_val(regs, inst[2])
            case _:
                print("Unkown argument", _)


def get_val(regs: dict, name: str):
    if name.strip("-").isdigit():
        return int(name)
    return regs[name]


if __name__ == "__main__":
    with open("example.txt", "r") as file:
        DATA = file.read().strip().splitlines()
        assert solve(DATA) == 4

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
        print(solve(DATA))
