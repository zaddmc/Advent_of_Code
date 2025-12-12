def solve(data):
    *shapes, things = data.split("\n\n")
    shapes = {int(s[0]): s.count("#") for s in shapes}
    things = things.splitlines()

    valid_entries = 0
    for t in things:
        dim, *vals = t.split(" ")
        vals = tuple(map(int, vals))
        w, h = map(int, dim.strip(":").split("x"))

        needed_area = 0
        for shape_idx, count in enumerate(vals):
            needed_area += shapes[shape_idx] * count

        if w * h >= needed_area:
            valid_entries += 1
    return valid_entries


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().strip()
        print(solve(DATA))
