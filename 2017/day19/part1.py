def solve(maze: list[str]):
    global output
    output = ""
    x = 0
    y = maze[x].index("|")
    dir = (1, 0)

    def traverse(x, y):
        global output
        while True:
            dx, dy = dir
            x += dx
            y += dy
            if maze[x][y].isalpha():
                output += maze[x][y]
            if maze[x][y] in ["+", " "]:
                return x, y

    def new_dir(x, y):
        dx, dy = dir
        if dx == 0:
            if x + 1 < len(maze) and maze[x + 1][y] != " ":
                return (1, 0)
            elif x > 0 and maze[x - 1][y] != " ":
                return (-1, 0)
            else:
                return (0, 0)
        if dy == 0:
            if y + 1 < len(maze[0]) and maze[x][y + 1] != " ":
                return (0, 1)
            elif y > 0 and maze[x][y - 1] != " ":
                return (0, -1)
            else:
                return (0, 0)

    while True:
        x, y = traverse(x, y)
        dir = new_dir(x, y)
        if dir == (0, 0):
            return output


if __name__ == "__main__":
    with open("example.txt", "r") as file:
        assert solve(file.read().splitlines()) == "ABCDEF"

    with open("input.txt", "r") as file:
        DATA = file.read().splitlines()
    print(solve(DATA))
