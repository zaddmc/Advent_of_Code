DATA: str = ""
with open("../../input/day09.txt", "r") as file:
    DATA = file.read()[:-1]


def expand(string: str, sectionize: bool) -> list[str]:
    cur_id: int = 0
    state: bool = True  # when true will use id
    new_str: list = []
    appender = new_str.append if sectionize else new_str.extend
    for char in string:
        if state:
            appender([str(cur_id) for _ in range(int(char))])

            state = False
            cur_id += 1
        else:
            appender(["." for _ in range(int(char))])

            state = True

    return new_str


def get_last_char(string: str, minus_i: int) -> int:
    if string[minus_i] == ".":
        return get_last_char(string, minus_i - 1)
    return minus_i


def collapse(string: list[str]) -> list[str]:
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


def reorder(string: list[list[str]]):
    for i_sec, section in enumerate(string.copy()[::-1]):
        if "." in section or section == []:
            continue
        for i_spot, spot in enumerate(string):
            if "." not in spot:
                continue
            if len(string) - (i_sec - 2) <= i_spot:
                break
            if len(spot) >= len(section):
                string[string.index(section, 0, len(string))] = [
                    "." for _ in range(len(section))
                ]
                string[i_spot] = [char for char in section]
                string.insert(
                    i_spot + 1, ["." for _ in range(len(spot) - len(section))]
                )
                string = concatenate(string)

                break
    return string


def concatenate(string: list[list[str]]) -> list[list[str]]:
    new_string = []
    prev_elm = []
    for elm in string:
        if "." in prev_elm and "." in elm:
            prev_elm.extend(elm)
            continue

        if elm == []:
            continue

        new_string.append(elm)
        prev_elm = elm
    return new_string


def simplify(string: list[list]) -> list:
    new_list: list = []
    for sub_list in string:
        new_list.extend(sub_list)
    return new_list


def checksum(string: list[str]) -> int:
    sum = 0
    for i, char in enumerate(string):
        if char == ".":
            continue
        sum += i * int(char)
    return sum


p1 = checksum(collapse(expand(DATA, False)))
print(f"{p1=}")

print(checksum(simplify(reorder(expand("2333133121414131402", True)))))
test_val = "2333133121414131402"
print(expand(test_val, True))
print(reorder(expand(test_val, True)))
print(simplify(reorder(expand(test_val, True))))
exit(0)
p2 = checksum(simplify(reorder(expand(DATA, True))))
print(f"{p2=}")
