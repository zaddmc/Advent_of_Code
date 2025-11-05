def solve(data):
    graph = {}

    for dat in data:
        node, paths = dat.split(" <->")
        graph[int(node)] = [int(p) for p in paths.split(",")]

    count = 0
    visited = set()
    for node, paths in graph.items():
        if node in visited:
            continue
        count += 1
        queue = set([node])
        while queue:
            node = queue.pop()
            visited.add(node)
            queue |= set(n for n in graph[node]) - queue - visited
    return count


if __name__ == "__main__":
    with open("example.txt", "r") as file:
        assert solve(file.read().strip().splitlines()) == 2

    with open("input.txt", "r") as file:
        print(solve(file.read().strip().splitlines()))
