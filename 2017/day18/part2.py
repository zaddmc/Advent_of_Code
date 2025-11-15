from collections import defaultdict


def solve(data):
    prog0 = Prog(0, data)
    prog1 = Prog(1, data)
    progs = [prog0, prog1]

    while True:
        for idx, pro in enumerate(progs):
            pro.run(prog0.output if pro == prog1 else prog1.output)

        # print(prog0.output, prog1.output)
        if len(prog0.output) == 0 and len(prog1.output) == 0:
            break
    return prog1.sent


class Prog:
    def __init__(self, id, instructions):
        self.instructions = instructions
        self.regs = defaultdict(int)
        self.regs["p"] = id
        self.ip = 0

        self.sent = 0
        self.output = []

    def run(self, incomming):
        while True:
            try:
                inst = self.instructions[self.ip].split()
            except:
                break
            self.ip += 1

            match inst[0]:
                case "snd":
                    self.output.append(get_val(self.regs, inst[1]))
                    self.sent += 1
                case "set":
                    self.regs[inst[1]] = get_val(self.regs, inst[2])
                case "add":
                    self.regs[inst[1]] += get_val(self.regs, inst[2])
                case "mul":
                    self.regs[inst[1]] *= get_val(self.regs, inst[2])
                case "mod":
                    self.regs[inst[1]] %= get_val(self.regs, inst[2])
                case "rcv":
                    if len(incomming) == 0:
                        self.ip -= 1
                        return self.output
                    self.regs[inst[1]] = incomming.pop(0)
                case "jgz":
                    if get_val(self.regs, inst[1]) > 0:
                        self.ip -= 1  # To counter the start
                        self.ip += get_val(self.regs, inst[2])
                case _:
                    print("Unkown argument", _)


def get_val(regs: dict, name: str):
    if name.strip("-").isdigit():
        return int(name)
    return regs[name]


if __name__ == "__main__":
    with open("example2.txt", "r") as file:
        DATA = file.read().strip().splitlines()
        assert solve(DATA) == 3

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
        print(solve(DATA))
