from collections import deque


def solve() -> tuple[int, int]:
    get_data(False)
    # p1 = brute_force()
    p1 = skipping(2)
    p2 = skipping(20)
    return (p1, p2)


def skipping(max_dist: int):
    start, end = find_endpoints()
    base_time, visited = BFS(start, end, MAP)
    cheats = 0
    threshold = 100

    path = sorted(visited, key=visited.get)
    for t2 in range(threshold, len(path)):
        for t1 in range(t2 - threshold):
            x1, y1 = path[t1]
            x2, y2 = path[t2]
            distance = abs(x1 - x2) + abs(y1 - y2)
            if distance <= max_dist and t2 - t1 - distance >= threshold:
                cheats += 1
    return cheats


def brute_force():
    start, end = find_endpoints()
    base_time, _ = BFS(start, end, MAP)
    options = 0

    for row, line in enumerate(MAP[1:-1]):
        for col, char in enumerate(line[1:-1]):
            if char == "#":
                map = MAP.copy()
                map[row + 1] = MAP[row + 1][: col + 1] + "." + MAP[row + 1][col + 2 :]
                new_time, _ = BFS(start, end, map)
                if base_time - new_time >= 100:
                    options += 1
    return options


def BFS(start, end, map):

    queue = deque([(0, start, dict())])

    while queue:
        score, (r, c), visited = queue.popleft()
        visited[(r, c)] = score

        if (r, c) == end:
            return score, visited

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (nr, nc) not in visited and map[nr][nc] != "#":
                queue.append((score + 1, (nr, nc), visited.copy()))
    return None


def pr_map(map):
    for line in map:
        print(line)


def get_data(test: bool):
    global MAP, SIZE
    if test:
        with open("../../input/day20exp.txt", "r") as file:
            MAP = file.read().splitlines()
    else:
        with open("../../input/day20.txt", "r") as file:
            MAP = file.read().splitlines()
    SIZE = len(MAP)


def find_endpoints():
    start = end = None
    for idx, line in enumerate(MAP):
        for idy, char in enumerate(line):
            if char == "S":
                start = (idx, idy)
                if end:
                    return start, end
            if char == "E":
                end = (idx, idy)
                if start:
                    return start, end


if __name__ == "__main__":
    print(solve())
