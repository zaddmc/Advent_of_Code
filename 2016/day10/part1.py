from collections import defaultdict


def solve(instructions: list[str]):
    memory: dict[str, list] = defaultdict(list)

    while len(instructions) > 0:
        start_len = len(instructions)
        for line in remaining(instructions):
            if line.startswith("value"):
                parts = line.split()
                memory["".join(parts[-2:])].append(int(parts[1]))
                instructions.remove(line)

            elif line.startswith("bot"):
                if handle_bot(memory, line):
                    instructions.remove(line)
            else:
                print("The world is dead")

        if len(instructions) == start_len:
            print("Nothing chagned, probalby")
            break

    return sum(memory["output0"]) * sum(memory["output1"]) * sum(memory["output2"])


def handle_bot(memory: dict[str, list], line: str) -> bool:
    parts = line.split()
    main_bot = memory["".join(parts[:2])]
    if len(main_bot) != 2:
        return False
    lower, higher = sorted(main_bot)
    if lower == 17 and higher == 61:
        print(parts[1])
    main_bot.clear()
    memory["".join(parts[5:7])].append(lower)
    memory["".join(parts[10:])].append(higher)
    return True


def remaining(lines: list[str]):
    for line in lines:
        yield line


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
