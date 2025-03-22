DATA = []
with open("../../input/day7.txt", "r") as file:
    for line in file.readlines():
        result, vals = line.split(":")
        new_vals = []
        for val in vals.split():
            new_vals.append(int(val))
        DATA.append((int(result), new_vals))


def step(pre_val, remaining_vals, result):
    add = pre_val + remaining_vals[0]
    mult = pre_val * remaining_vals[0]

    if len(remaining_vals) == 1:
        return result in (add, mult)

    return step(add, remaining_vals[1:], result) | step(
        mult, remaining_vals[1:], result
    )


def stepcat(pre_val: int, remaining_vals: list[int], result: int) -> bool:
    add = pre_val + remaining_vals[0]
    mult = pre_val * remaining_vals[0]
    con = int(str(pre_val) + str(remaining_vals[0]))

    if len(remaining_vals) == 1:
        return result in (add, mult, con)

    return (
        stepcat(add, remaining_vals[1:], result)
        | stepcat(mult, remaining_vals[1:], result)
        | stepcat(con, remaining_vals[1:], result)
    )


p1 = 0
p2 = 0
for result, vals in DATA:
    if step(vals[0], vals[1:], result):
        p1 += result

    if stepcat(vals[0], vals[1:], result):
        p2 += result

print(p1)
print(p2)
