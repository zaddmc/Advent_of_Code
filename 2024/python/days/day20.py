from heapq import heappop, heappush


def solve() -> tuple[int, int]:
    get_data(False)
    p1 = brute_force()
    return (p1, -1)


def brute_force():
    start, end = find_endpoints()
    base_time = BFS(start, end, MAP)
    options = 0

    for row, line in enumerate(MAP[1:-1]):
        for col, char in enumerate(line[1:-1]):
            if char == "#":
                map = MAP.copy()
                map[row + 1] = MAP[row + 1][: col + 1] + "." + MAP[row + 1][col + 2 :]
                new_time = BFS(start, end, map)
                if base_time - new_time >= 100:
                    options += 1
    return options


def BFS(start, end, map):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    pque = [(0, start)]
    visited = set()
    visited.add(start)

    while pque:
        score, (r, c) = heappop(pque)

        if (r, c) == end:
            return score

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and map[nr][nc] == ".":
                heappush(pque, (score + 1, (nr, nc)))
                visited.add((nr, nc))
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
