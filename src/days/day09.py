DATA: str = ""
with open("../../input/day9.txt", "r") as file:
    DATA = file.read()[:-1]


def expand(string: str) -> list[str]:
    cur_id: int = 0
    state: bool = True  # when true will use id
    new_str: list[str] = []
    for char in string:
        if state:
            new_str.extend([str(cur_id) for _ in range(int(char))])

            state = False
            cur_id += 1
        else:
            new_str.extend(["." for _ in range(int(char))])

            state = True
    return new_str


def get_last_char(string: str, minus_i: int) -> int:
    if string[minus_i] == ".":
        return get_last_char(string, minus_i - 1)
    return minus_i


def collapse(string: list[str]) -> str:
    new_str: list[str] = []
    minus_i = -1
    for i in range(len(string) - string.count(".")):
        if string[i] == ".":
            minus_i = get_last_char(string, minus_i)
            new_str.append(string[minus_i])
            minus_i -= 1
        else:
            new_str.append(string[i])

    new_str.extend(["." for _ in range(len(string) - len(new_str))])
    return new_str


def checksum(string: list[str]) -> int:
    sum = 0
    for i, char in enumerate(string):
        if char == ".":
            break
        sum += i * int(char)

    return sum


p1 = checksum(collapse(expand(DATA)))
print(f"{p1=}")
