def solve(mdist):
    arr = [0]
    cur_pos = 0
    for itt in range(1, 2018):
        cur_pos = (cur_pos + mdist) % len(arr)
        arr.insert(cur_pos + 1, itt)
        cur_pos += 1

    return arr[arr.index(2017) + 1]


if __name__ == "__main__":
    assert solve(3) == 638

    with open("input.txt", "r") as file:
        DATA = int(file.read().strip())
    print(solve(DATA))
