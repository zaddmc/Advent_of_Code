from collections import defaultdict
from string import ascii_lowercase


def solve(rooms):

    for room in rooms:
        *words, control = room[:-1].split("-")
        sec_id, control_letters = control.split("[")
        words = "".join(words)
        sec_id = int(sec_id)

        if is_decoy(words, control):
            continue

        new_word = ""
        for letter in words:
            org_idx = ascii_lowercase.find(letter)
            new_word += ascii_lowercase[(org_idx + sec_id) % len(ascii_lowercase)]
        if "north" in new_word:
            return sec_id


def is_decoy(words: str, control_letters: str):
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

    return letters == control_letters


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
