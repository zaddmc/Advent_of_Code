def solve(ranges):
    ranges = ranges.split(",")
    val = 0
    for ran in ranges:
        val += sum(does_repeat(ran))
    return val


def does_repeat(value):
    lhs, rhs = value.split("-")
    r_val = set()
    for val in range(int(lhs), int(rhs) + 1):
        val = str(val)

        for i in range(1, len(val)):
            ss = val[:i]
            if val.count(ss) > 1:
                temp = val.replace(ss, "")
                if len(temp) == 0:
                    r_val.add(int(val))
    return r_val


if __name__ == "__main__":
    test_val = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    assert solve(test_val) == 4174379265

    with open("input.txt", "r") as file:
        DATA = file.read().strip()
    print(solve(DATA))
