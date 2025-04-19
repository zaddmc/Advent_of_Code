def solve():
    get_data(False)
    robots = list(interpret_data())
    pr_map(robots, False)
    for i in range(10000):
        imply_movement(robots, 1)
        if pr_map(robots, False):
            p2 = i + 1
            break
        if i == 100:
            p1 = get_safety(robots)
    return (p1, p2)


def get_safety(robots: list) -> int:
    q1 = q2 = q3 = q4 = 0

    for robot in robots:
        x, y = robot.pos
        if x < WIDTH // 2:
            if y < HEIGHT // 2:
                q1 += 1
            elif y > HEIGHT // 2:
                q3 += 1
        elif x > WIDTH // 2:
            if y < HEIGHT // 2:
                q2 += 1
            elif y > HEIGHT // 2:
                q4 += 1

    # print(q1, q2, q3, q4)
    return q1 * q2 * q3 * q4


def imply_movement(robots: list, time: int):
    for robot in robots:
        robot.move(time)


def interpret_data():
    for line in DATA:
        yield Robot(line)


def get_data(test: bool):
    global DATA, WIDTH, HEIGHT
    if test:
        DATA = [
            "p=0,4 v=3,-3",
            "p=6,3 v=-1,-3",
            "p=10,3 v=-1,2",
            "p=2,0 v=2,-1",
            "p=0,0 v=1,3",
            "p=3,0 v=-2,-2",
            "p=7,6 v=-1,-3",
            "p=3,0 v=-1,-2",
            "p=9,3 v=2,3",
            "p=7,3 v=-1,2",
            "p=2,4 v=2,-3",
            "p=9,5 v=-3,-3",
        ]
        WIDTH = 11
        HEIGHT = 7

    else:
        with open("../../input/day14.txt", "r") as file:
            DATA = file.read().strip().splitlines()
        WIDTH = 101
        HEIGHT = 103


class Robot:
    def __init__(self, intial: str):
        position, velocity = intial.split()
        px, py = position.split(",")
        self.pos: tuple[int, int] = (int(px[2:]), int(py))

        vx, vy = velocity.split(",")
        self.vel: tuple[int, int] = (int(vx[2:]), int(vy))

    def __str__(self):
        return f"pos={self.pos}, vel={self.vel}"

    def move(self, times: int = 1):
        self.pos = tup_add(self.pos, tup_mul(self.vel, times))

        x, y = self.pos
        self.pos = (x % WIDTH, y % HEIGHT)


def tup_mul(tup: tuple[int, int], mul: int) -> tuple[int, int]:
    return (tup[0] * mul, tup[1] * mul)


def tup_add(tup1: tuple[int, int], tup2: tuple[int, int]) -> tuple[int, int]:
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])


def pr_robots(robots: list):
    for robot in robots:
        print(robot)


def pr_map(robots: list, prin: bool):
    map = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for robot in robots:
        x, y = robot.pos
        map[y][x] += 1
    counter = 0
    flag = False

    for hei, line in enumerate(map):
        for wid, val in enumerate(line):
            if val == 0:
                if prin:
                    if wid == WIDTH // 2:
                        print("|", end="")
                    elif hei == HEIGHT // 2:
                        print("-", end="")
                    else:
                        print(".", end="")
                counter = 0
            else:
                if prin:
                    print(val, end="")
                counter += 1
                if counter > 8:
                    flag = True

        if prin:
            print()
    return flag


if __name__ == "__main__":
    print(solve())
