from collections import deque


def solve() -> tuple[int, int]:
    get_data(False)
    # p1 = brute_force()
    p1 = skipping()
    return (p1, -1)


def skipping():
    start, end = find_endpoints()
    base_time, visited = BFS(start, end, MAP)
    options = 0

    for (r, c), score in visited.items():
        for nr, nc in [(r + 2, c), (r - 2, c), (r, c + 2), (r, c - 2)]:
            if visited.get((nr, nc), 0) - score >= 102:
                options += 1
    return options


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
            if (nr, nc) not in visited and map[nr][nc] == ".":
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
    global MAP
    start = end = None
    for idx, line in enumerate(MAP):
        for idy, char in enumerate(line):
            if char == "S":
                start = (idx, idy)
                MAP[idx] = MAP[idx].replace("S", ".")
                if end:
                    return start, end
            if char == "E":
                end = (idx, idy)
                MAP[idx] = MAP[idx].replace("E", ".")
                if start:
                    return start, end


if __name__ == "__main__":
    print(solve())
