import re


def solve() -> tuple[int, int]:
    get_data()
    p1 = max(calc())
    p2 = simulate()
    return (p1, p2)


def simulate():
    score = {r[0]: 0 for r in DATA}
    distance = {r[0]: 0 for r in DATA}
    stats = {r[0]: r[1:] for r in DATA}

    for sec in range(2503):
        for name, (speed, active, passive) in stats.items():
            speed, active, passive = int(speed), int(active), int(passive)
            if sec % (active + passive) < active:
                distance[name] += speed

        high = distance[max(distance, key=distance.get)]
        for name, dist in distance.items():
            if dist == high:
                score[name] += 1

    return score[max(score, key=score.get)]


def calc():
    time = 2503
    for name, speed, active, passive in DATA:
        speed, active, passive = int(speed), int(active), int(passive)

        full_cycles, left_over = divmod(time, active + passive)

        distance = full_cycles * active * speed
        if left_over - active <= 0:
            distance += (active - left_over) * speed
        yield distance


def get_data():
    global DATA
    rune = r"^(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds.$"
    with open("../../input/day14.txt", "r") as file:
        DATA = file.read().splitlines()
    DATA = list(map(lambda s: re.findall(rune, s)[0], DATA))


if __name__ == "__main__":
    print(solve())
