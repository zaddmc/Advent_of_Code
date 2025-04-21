def solve() -> tuple[int, int]:
    global Marked
    get_data(True)
    Marked = []
    p1 = BFS(find_maze("S"), ">")
    return (p1, -1)


def BFS(pos: tuple[int, int], dir: str):
    # print(pos, dir, maze_tup(pos))
    # input()

    if pos in Marked:
        return 0
    Marked.append(pos)

    match maze_tup(pos):
        case "#":
            return 0
        case "E":
            return 1
        case "." | "S":
            left, straight, right = [
                BFS(tup_add(pos, turn(dir, c)), turn(dir, c)) for c in range(-1, 2)
            ]

            plist = []
            if left:
                plist.append(left + 1000)
            if straight:
                plist.append(straight + 1)
            if right:
                plist.append(right + 1000)

            if len(plist) != 0:
                return min(plist)
            return 0
        case _ as a:
            raise Exception(f"Unknown char: '{a}'")


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
            "###############",
            "#.......#....E#",
            "#.#.###.#.###.#",
            "#.....#.#...#.#",
            "#.###.#####.#.#",
            "#.#.#.......#.#",
            "#.#.#####.###.#",
            "#...........#.#",
            "###.#.#####.#.#",
            "#...#.....#.#.#",
            "#.#.#.###.#.#.#",
            "#.....#...#.#.#",
            "#.###.#.#.#.#.#",
            "#S..#.....#...#",
            "###############",
        ]
    else:
        with open("../../input/day16.txt", "r") as file:
            MAZE = file.read().strip().splitlines()


if __name__ == "__main__":
    print(solve())
