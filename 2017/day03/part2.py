from spiral import gen_spiral


def count_neighbors(matrix, idx, idy):
    neighbors = []
    rows, cols = len(matrix), len(matrix[0])

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # skip the center cell itself
            nx, ny = idx + dx, idy + dy
            if 0 <= nx < rows and 0 <= ny < cols and isinstance(matrix[nx][ny], tuple):
                neighbors.append(matrix[nx][ny])
    return sum(map(lambda a: a[1], neighbors))


def find_val(matrix, target):
    for idx, row in enumerate(matrix):
        for idy, val in enumerate(row):
            if val == target:
                return idx, idy


def solve(matrix, target):
    x, y = find_val(matrix, 1)
    matrix[x][y] = (1, 1)
    for n in range(2, int(target**0.5)):
        x, y = find_val(matrix, n)
        new_val = count_neighbors(matrix, x, y)
        if new_val > target:
            return new_val
        matrix[x][y] = (n, new_val)


if __name__ == "__main__":
    with open("./input.txt", "r") as file:
        DATA = int(file.read().strip())

    matrix = gen_spiral(int(DATA**0.5))
    print(solve(matrix, DATA))
