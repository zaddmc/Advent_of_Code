from collections import deque


def solve(seed):
    my_map = set()

    for x in range(50):
        for y in range(50):
            if is_open(seed, x, y):
                my_map.add((x, y))
    ret = bfs(my_map)
    print_map(my_map, ret)
    print(sorted(ret))
    return len(ret)


def bfs(spaces):
    not_visited: deque = deque()
    not_visited.append((0, (1, 1)))
    visited = set()

    while not_visited:
        score, (r, c) = not_visited.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))

        if score > 49:
            return visited

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (nr, nc) not in visited and (nr, nc) in spaces:
                not_visited.append((score + 1, (nr, nc)))
    return []


def is_open(seed, x, y) -> bool:
    val = (x * x + 3 * x + 2 * x * y + y + y * y) + seed
    ones = bin(val).count("1")
    return ones % 2 == 0


def print_map(open_spaces, visited):
    for y in range(50):
        for x in range(50):
            if (x, y) in visited:
                char = "*"
            elif (x, y) in open_spaces:
                char = "."
            else:
                char = "#"
            print(char, end="")
        print()


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        data = int(file.read().strip())
    print(solve(data))
