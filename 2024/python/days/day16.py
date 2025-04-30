import sys
from collections import deque

sys.setrecursionlimit(10000)


def solve() -> tuple[int, int]:
    global Marked
    get_data(True)
    Marked = []
    # p1 = BFS(find_maze("S"), ">", Marked) - 1
    # p1 = Dijkstra(find_maze("S"), find_maze("E"))
    p1 = shortest_safe_path(find_maze("S"), find_maze("E"))
    return (p1, -1)


def shortest_safe_path(start, end):
    directions = [(-1, 0, "^"), (1, 0, "v"), (0, -1, "<"), (0, 1, ">")]
    rows, cols = len(MAZE), len(MAZE[0])

    # BFS setup
    queue = deque([(start[0], start[1], ">", 0)])  # (row, col, dir, path_length)
    visited = set()
    visited.add((0, 0))

    while queue:
        r, c, dir, length = queue.popleft()

        if (r, c) == end:
            return length

        for dr, dc, ndir in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if MAZE[nr][nc] in ".ES":
                    visited.add((nr, nc))
                    val_add = 1 if dir == ndir else 1001
                    queue.append((nr, nc, ndir, length + val_add))

    return None  # No path found


def BFS(pos: tuple[int, int], dir: str, marked: list):
    # print(pos, dir, maze_tup(pos), end="")
    # input()

    if pos in marked:
        return 0
    marked.append(pos)

    match maze_tup(pos):
        case "#":
            return 0
        case "E":
            return 1
        case "." | "S":
            left, straight, right = [
                BFS(tup_add(pos, turn(dir, c)), turn(dir, c), marked.copy())
                for c in range(-1, 2)
            ]

            plist = []
            if left:
                plist.append(left + 1001)
            if straight:
                plist.append(straight + 1)
            if right:
                plist.append(right + 1001)

            if len(plist) != 0:
                return min(plist)
            return 0
        case _ as a:
            raise Exception(f"Unknown char: '{a}'")


def Dijkstra(source: tuple[int, int], dest: tuple[int, int]):
    closed_set = {}
    open_set = {source: 0}
    dir_set = {source: ">"}
    current = source
    cur_dist = open_set[source]

    while current != dest:
        if len(open_set) == 0:
            raise Exception("No Path found")

        current, cur_dist = find_next(open_set)
        open_set.pop(current)
        closed_set[current] = cur_dist

        dir_list = ["<", "^", ">", "v"]
        for neighbor, dir in zip([tup_add(current, dir) for dir in dir_list], dir_list):
            if neighbor in closed_set.keys() or neighbor in open_set.keys():
                continue
            if maze_tup(neighbor) == "#":
                continue

            dir_set[neighbor] = dir
            if dir_set[current] == dir:
                open_set[neighbor] = cur_dist + 1
            else:
                open_set[neighbor] = cur_dist + 1001

    return cur_dist


def find_next(mdict: dict[tuple, int]):
    current, cur_dist = list(mdict.items())[0]
    for pot, pot_dist in mdict.items():
        if pot_dist < cur_dist:
            current = pot
            cur_dist = mdict[pot]
    return current, mdict[current]


DIRECTION_DICT = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}


def turn(dir: str, offset: int):
    dir_list = "<^>v"
    return dir_list[(dir_list.index(dir, 0, 4) + offset) % 4]


def tup_add(tup1: tuple[int, int], tup2: tuple[int, int]) -> tuple[int, int]:
    if isinstance(tup2, str):
        tup2 = DIRECTION_DICT[tup2]
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])


def maze_tup(tup):
    return MAZE[tup[0]][tup[1]]


def find_maze(target: str):
    for idx, line in enumerate(MAZE):
        for idy, char in enumerate(line):
            if char == target:
                return (idx, idy)


def get_data(test: bool):
    global MAZE
    if test:
        MAZE = [
            "#################",
            "#...#...#...#..E#",
            "#.#.#.#.#.#.#.#.#",
            "#.#.#.#...#...#.#",
            "#.#.#.#.###.#.#.#",
            "#...#.#.#.....#.#",
            "#.#.#.#.#.#####.#",
            "#.#...#.#.#.....#",
            "#.#.#####.#.###.#",
            "#.#.#.......#...#",
            "#.#.###.#####.###",
            "#.#.#...#.....#.#",
            "#.#.#.#####.###.#",
            "#.#.#.........#.#",
            "#.#.#.#########.#",
            "#S#.............#",
            "#################",
        ]
    else:
        with open("../../input/day16.txt", "r") as file:
            MAZE = file.read().strip().splitlines()


if __name__ == "__main__":
    print(solve())
