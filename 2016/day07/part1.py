def solve(ips):
    counter = 0
    for ip in ips:
        if abba_filter(ip):
            counter += 1
    return counter


def abba_filter(string: str):
    in_brackets = False
    found_abba = False
    for i in range(len(string) - 3):
        # True if abba in view
        if "[" in string[i : i + 3]:
            in_brackets = True
            continue
        if "]" in string[i : i + 3]:
            in_brackets = False
            continue
        if (
            string[i] != string[i + 1]
            and string[i] == string[i + 3]
            and string[i + 1] == string[i + 2]
        ):
            if in_brackets:
                return False
            found_abba = True
    return found_abba


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
