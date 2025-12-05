def solve(ranges):
    ranges = set(tuple(map(int, r.split("-"))) for r in ranges)

    stay_alive = True
    while stay_alive:
        for ran in ranges:
            ret = is_in(ranges, ran, ran[0])
            if ret:
                ranges.remove(ran)
                ranges.remove(ret)
                ranges.add((min(ran[0], ret[0]), max(ran[1], ret[1])))

                break
        else:
            break

    valid_ids = 0
    for ran in ranges:
        valid_ids += ran[1] - ran[0] + 1
    return valid_ids


def is_in(ranges, ignore, value):
    for ran in ranges:
        if ran[0] <= value <= ran[1]:
            if ran == ignore:
                continue
            return ran


if __name__ == "__main__":
    ranges = ["3-5", "10-14", "16-20", "12-18"]
    assert solve(ranges) == 14

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
        split_id = DATA.index("")
        ranges = DATA[:split_id]
        print(solve(ranges))
