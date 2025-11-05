def solve(data):
    graph = {}

    for dat in data:
        node, paths = dat.split(" <->")
        graph[int(node)] = [int(p) for p in paths.split(",")]

    count = 0
    queue = set([0])
    visited = set()
    while queue:
        node = queue.pop()
        visited.add(node)
        queue |= set(n for n in graph[node]) - queue - visited
        count += 1
    return count


if __name__ == "__main__":
    with open("example.txt", "r") as file:
        assert solve(file.read().strip().splitlines()) == 6

    with open("input.txt", "r") as file:
        print(solve(file.read().strip().splitlines()))
