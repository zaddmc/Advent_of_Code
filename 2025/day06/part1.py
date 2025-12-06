def solve(data):
    data = [data[i].split() for i in range(len(data))]
    total = 0
    for i in range(len(data[0])):
        string = data[-1][i].join([data[j][i] for j in range(len(data) - 1)])
        total += eval(string)
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
