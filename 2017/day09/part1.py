def solve(data):

    open_groups = 0
    score = 0

    garbage_flag = False

    i = 0
    while i < len(data):
        ch = data[i]

        match ch:
            case "!":
                i += 1
            case "<":
                garbage_flag = True
            case ">":
                garbage_flag = False
            case "{":
                open_groups += 1 if not garbage_flag else 0
            case "}":
                score += open_groups if not garbage_flag else 0
                open_groups += -1 if not garbage_flag else 0

        i += 1
    return score


if __name__ == "__main__":
    assert solve("{}") == 1
    assert solve("{{{}}}") == 6
    assert solve("{{},{}}") == 5
    assert solve("{{{},{},{{}}}}") == 16
    assert solve("{<a>,<a>,<a>,<a>}") == 1
    assert solve("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
    assert solve("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
    assert solve("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3

    with open("input.txt", "r") as file:
        data = file.read().strip()
    print(solve(data))
