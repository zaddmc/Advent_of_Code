from collections import deque


def solve(seed, tup):
    my_map = set()

    for x in range(50):
        for y in range(50):
            if is_open(seed, x, y):
                my_map.add((x, y))
    ret = bfs(my_map, tup)
    return ret


def bfs(spaces, target) -> int:
    tar_x, tar_y = target
    not_visited: deque = deque()
    not_visited.append([0, (1, 1), dict()])

    while not_visited:
        score, (r, c), visited = not_visited.popleft()
        visited[r, c] = score

        if (r, c) == target:
            return score

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (nr, nc) not in visited and (nr, nc) in spaces:
                not_visited.append((score + 1, (nr, nc), visited.copy()))

    return -1


def is_open(seed, x, y) -> bool:
    val = (x * x + 3 * x + 2 * x * y + y + y * y) + seed
    ones = bin(val).count("1")
    return ones % 2 == 0


def print_map(open_spaces):
    for y in range(10):
        for x in range(10):
            print("." if (x, y) in open_spaces else "#", end="")
        print()


if __name__ == "__main__":
    assert solve(10, (7, 4)) == 11

    with open("./input.txt", "r") as file:
        data = int(file.read().strip())
    print(solve(data, (31, 39)))
