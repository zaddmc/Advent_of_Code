def solve() -> tuple[int, int]:
    get_data()
    p1 = find_aunt()
    p2 = find_aunt_adv()
    return (p1, p2)


def find_aunt():
    for aunt, aunt_vals in DATA.items():
        correct = 0
        for item, count in aunt_vals.items():
            if KNOWN_ITMES[item] == count:
                correct += 1
        if correct == 3:
            return aunt


def find_aunt_adv():
    for aunt, aunt_vals in DATA.items():
        correct = 0
        for item, count in aunt_vals.items():
            match item:
                case "cats" | "trees":
                    if KNOWN_ITMES[item] < count:
                        correct += 1
                case "pomeranians" | "goldfish":
                    if KNOWN_ITMES[item] > count:
                        correct += 1
                case _:
                    if KNOWN_ITMES[item] == count:
                        correct += 1
        if correct == 3:
            return aunt


def get_data():
    global DATA, KNOWN_ITMES
    with open("../../input/day16.txt", "r") as file:
        rawdata = file.read().splitlines()

    DATA = {}
    for s in rawdata:
        s = s.replace(":", "")
        s = s.replace(",", "")
        s = s.split(" ")
        DATA[int(s[1])] = {s[k]: int(s[k + 1]) for k in range(2, 8, 2)}

    KNOWN_ITMES = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }


if __name__ == "__main__":
    print(solve())
