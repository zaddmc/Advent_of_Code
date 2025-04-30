import heapq
import sys
from collections import deque

sys.setrecursionlimit(10000)


def solve() -> tuple[int, int]:
    global Marked
    get_data(False)
    # p1 = BFS(find_maze("S"), ">", set()) - 1
    # p1 = Dijkstra(find_maze("S"), find_maze("E"))

    paths = list(shortest_safe_path(find_maze("S"), find_maze("E")))
    p1 = paths[0][-1]

    seats = set()
    for path in paths:
        seats |= set(path[0])
    p2 = len(seats)
    return (p1, p2)


def shortest_safe_path(start, end):
    directions = [(-1, 0, "^"), (0, 1, ">"), (1, 0, "v"), (0, -1, "<")]

    pque = [(0, (*start, ">"), [start])]
    visited = {}
    best_score = 9999999

    while pque and pque[0][0] <= best_score:
        score, (r, c, dir), path = heapq.heappop(pque)

        if (r, c) == end:
            best_score = score
            yield path, score
            continue

        if (r, c, dir) in visited.keys() and visited[(r, c, dir)] < score:
            continue
        visited[(r, c, dir)] = score

        for dr, dc, ndir in directions:
            nr, nc = r + dr, c + dc
            if MAZE[nr][nc] in ".ES":
                cost = 1 if dir == ndir else 1001
                heapq.heappush(pque, (score + cost, (nr, nc, ndir), path + [(nr, nc)]))


def BFS(pos: tuple[int, int], dir: str, visited: set):
    # print(pos, dir, maze_tup(pos), end="")
    # input()

    if pos in visited:
        return 0
    visited.add(pos)

    match maze_tup(pos):
        case "#":
            return 0
        case "E":
            return 1
        case "." | "S":
            left, straight, right = [
                BFS(tup_add(pos, turn(dir, c)), turn(dir, c), visited)
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
    print(closed_set)
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
            MAZE = file.read().splitlines()


if __name__ == "__main__":
    print(solve())
