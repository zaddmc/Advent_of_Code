from collections import deque


def solve() -> tuple[int, int]:
    get_data(False)
    make_map()
    p1 = shortest_safe_path()
    return (p1, -1)


def shortest_safe_path():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    # BFS setup
    queue = deque([(0, 0, 0)])  # (row, col, path_length)
    visited = set()
    visited.add((0, 0))

    while queue:
        r, c, length = queue.popleft()

        if (r, c) == (SIZE - 1, SIZE - 1):
            return length

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < SIZE and 0 <= nc < SIZE and (nr, nc) not in visited:
                if MAP[nr][nc] == ".":
                    queue.append((nr, nc, length + 1))
                    visited.add((nr, nc))

    return -1  # No path found


def make_map():
    global MAP
    MAP = [["." for _ in range(SIZE)] for _ in range(SIZE)]
    for num, line in enumerate(DATA):
        if num == BYTES:
            break
        x, y = list(map(int, line.split(",")))
        MAP[y][x] = "#"


def get_data(test: bool):
    global DATA, SIZE, BYTES
    if test:
        SIZE = 7
        BYTES = 12
        DATA = [
            "5,4",
            "4,2",
            "4,5",
            "3,0",
            "2,1",
            "6,3",
            "2,4",
            "1,5",
            "0,6",
            "3,3",
            "2,6",
            "5,1",
            "1,2",
            "5,5",
            "2,5",
            "6,5",
            "1,4",
            "0,4",
            "6,4",
            "1,1",
            "6,1",
            "1,0",
            "0,5",
            "1,6",
            "2,0",
        ]
    else:
        SIZE = 71
        BYTES = 1024
        with open("../../input/day18.txt", "r") as file:
            DATA = file.read().splitlines()


def pr_map():
    for line in MAP:
        for char in line:
            print(char, end="")
        print()


if __name__ == "__main__":
    print(solve())
