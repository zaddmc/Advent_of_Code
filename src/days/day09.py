DATA: str = ""
with open("../../input/day9.txt", "r") as file:
    DATA = file.read()[:-1]


def expand(string: str) -> str:
    cur_id: int = 0
    state: bool = True  # when true will use id
    new_str: str = ""
    for char in string:
        if state:
            new_str += str(cur_id) * int(char)

            state = False
            cur_id += 1
        else:
            new_str += "." * int(char)

            state = True
    return new_str


def get_last_char(string: str, minus_i: int) -> int:
    if string[minus_i] == ".":
        return get_last_char(string, minus_i - 1)
    return minus_i


def collapse(string: str) -> str:
    new_str: str = ""
    minus_i = -1
    for i in range(len(string) - string.count(".", 0, len(string))):
        if string[i] == ".":
            minus_i = get_last_char(string, minus_i)
            new_str += string[minus_i]
            minus_i -= 1
        else:
            new_str += string[i]

    new_str += "." * (len(string) - len(new_str))
    return new_str


def checksum(string: int) -> int:
    sum = 0
    for i, char in enumerate(string):
        if char == ".":
            break
        sum += i * int(char)

    return sum


print(collapse(expand(DATA)))
p1 = checksum(collapse(expand(DATA)))
print(f"{p1=}")
