def solve() -> tuple[int, int]:
    global Output, IP
    get_data(True)
    Output = []
    IP = 0

    tests()
    return (-1, -1)


def compute(opcode: int, operand: int):
    global REG_A, REG_B, REG_C, IP
    ip_changed = False
    match opcode:
        case 0:  # adv
            REG_A = REG_A / pow(2, com_operand(operand))
        case 1:  # bxl
            REG_B = REG_B ^ operand
        case 2:  # bst
            REG_B = com_operand(operand) % 8
        case 3:  # jnz
            if REG_A != 0:
                IP = operand
                ip_changed = True
        case 4:  # bxc
            REG_B = REG_B ^ REG_C
        case 5:  # out
            Output.append(com_operand(operand) % 8)
        case 6:  # bdv
            REG_B = REG_A / pow(2, com_operand(operand))
        case 7:  # cdv
            REG_C = REG_A / pow(2, com_operand(operand))

    if not ip_changed:
        IP += 2


def com_operand(operand):
    match operand:
        case num if num in range(4):
            return operand
        case 4:
            return REG_A
        case 5:
            return REG_B
        case 6:
            return REG_C
        case 7:
            return 7


def tests():
    global REG_A, REG_B, REG_C, PROG, Output

    # Test 1
    REG_C = 9
    compute(2, 6)
    print(REG_B)

    # Test 2
    REG_A = 10
    compute(5, 0)
    compute(5, 1)
    compute(5, 4)
    print(Output)

    # Test 3
    Output = []
    REG_A = 2024


def get_data(test: bool):
    global REG_A, REG_B, REG_C, PROG
    if test:
        data = [
            "Register A: 729",
            "Register B: 0",
            "Register C: 0",
            "",
            "Program: 0,1,5,4,3,0",
        ]
    else:
        with open("../../input/day17.txt", "r") as file:
            data = file.read().splitlines()

    REG_A, REG_B, REG_C = [int(dat.split(": ")[1]) for dat in data[:-2]]
    PROG = list(map(int, data[-1].split(": ")[1].split(",")))


if __name__ == "__main__":
    print(solve())
