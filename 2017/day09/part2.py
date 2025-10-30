def solve(data):

    score = 0
    garbage_flag = False

    i = 0
    while i < len(data):
        ch = data[i]

        match ch:
            case "!":
                i += 1
            case "<":
                score += 1 if garbage_flag else 0
                garbage_flag = True
            case ">":
                garbage_flag = False
            case _:
                score += 1 if garbage_flag else 0

        i += 1
    return score


if __name__ == "__main__":
    assert solve("<>") == 0
    assert solve("<random characters>") == 17
    assert solve("<<<<>") == 3
    assert solve("<{!>}>") == 2
    assert solve("<!!>") == 0
    assert solve("<!!!>>") == 0
    assert solve('<{o"i!a,<{i<a>') == 10

    with open("input.txt", "r") as file:
        data = file.read().strip()
    print(solve(data))
