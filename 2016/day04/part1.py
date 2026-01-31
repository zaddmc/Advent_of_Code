from collections import defaultdict


def solve(rooms):
    sector_sum = 0

    for room in rooms:
        *words, control = room[:-1].split("-")
        sec_id, control_letters = control.split("[")
        words = "".join(words)

        memory = defaultdict(int)
        for letter in words:
            memory[letter] += 1

        converted = []
        for key, value in memory.items():
            converted.append((-value, key))
        converted = sorted(converted)

        letters = ""
        for _, letter in converted[:5]:
            letters += letter

        if letters == control_letters:
            sector_sum += int(sec_id)

    return sector_sum


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
