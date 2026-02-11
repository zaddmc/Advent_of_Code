# Note the values become text: EOARGPHYAO


def solve(instructions):
    screen = [[False for _ in range(50)] for _ in range(6)]
    for inst in instructions:
        parts = inst.split()

        if parts[0] == "rect":
            x, y = tuple(map(int, parts[1].split("x")))
            for idx in range(x):
                for idy in range(y):
                    screen[idy][idx] = True

        elif parts[1] == "row":
            row = int(parts[2][2:])
            by = int(parts[4])
            screen[row] = screen[row][-by:] + screen[row][:-by]

        elif parts[1] == "column":
            col = int(parts[2][2:])
            by = int(parts[4])
            cols = [row[col] for row in screen]
            for i, val in enumerate(cols):
                screen[(i + by) % 6][col] = val

    on_pixels = 0
    for line in screen:
        on_pixels += line.count(True)
    print(on_pixels)
    print_screen(screen)


def print_screen(screen):
    for line in screen:
        for val in line:
            print("█" if val else " ", end="")
        print()


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    solve(DATA)
