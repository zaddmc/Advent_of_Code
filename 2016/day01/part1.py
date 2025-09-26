with open("./input.txt", "r") as file:
    DATA = file.read().strip().split(", ")

x = y = my_dir = 0

for dat in DATA:
    if dat[0] == "R":
        my_dir += 1
    else:
        my_dir += -1

    my_dir %= 4

    val = int(dat[1:])
    val = val if my_dir <= 1 else -val

    if my_dir % 2 == 0:
        x += val
    else:
        y += val

print(abs(x) + abs(y))
