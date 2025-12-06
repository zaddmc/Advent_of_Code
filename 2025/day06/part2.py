def solve(data):
    total = 0
    numbers = []
    for i in range(len(data[-1])):
        operator = data[-1][i] if data[-1][i] != " " else operator
        new_number = "".join(
            [data[j][i] for j in range(len(data) - 1) if data[j][i] != " "]
        )
        if new_number == "":
            total += eval(operator.join(numbers))
            numbers.clear()
        else:
            numbers.append(new_number)
    else:
        total += eval(operator.join(numbers))

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().splitlines()
    print(solve(DATA))
