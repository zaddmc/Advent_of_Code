import re


def solve(data):
    particles = [Particle(dat) for dat in data]
    for _ in range(1000):
        for particle in particles:
            particle.move()
    print(min([p.get_manhatten_dist() for p in particles]))


class Particle:
    Next_id = 0

    def __init__(self, data: str):
        self.id = Particle.Next_id
        Particle.Next_id += 1

        rune = r"^p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>$"
        res = re.match(rune, data).groups()
        res = tuple(map(int, res))
        self.posistion = res[0:3]
        self.velocity = res[3:6]
        self.acceleration = res[6:9]

    def get_manhatten_dist(self):
        return sum(map(lambda p: abs(p), self.posistion)), self.id

    def get_manhatten_veloc(self):
        return sum(map(lambda p: abs(p), self.velocity)), self.id

    def get_manhatten_accel(self):
        return sum(map(lambda p: abs(p), self.acceleration)), self.id

    def get_manhattens(self):
        return (
            self.get_manhatten_accel()[0],
            self.get_manhatten_veloc()[0],
            self.get_manhatten_dist()[0],
            self.id,
        )

    def move(self):
        self.velocity = tuple(map(lambda v, a: v + a, self.velocity, self.acceleration))
        self.posistion = tuple(
            map(lambda p, v: p + v, self.posistion, self.acceleration)
        )

    def __str__(self):
        return f"id={self.id}  p=<{self.posistion}>, v=<{self.velocity}>, a=<{self.acceleration}>"


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
