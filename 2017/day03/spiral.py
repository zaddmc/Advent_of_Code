def gen_spiral(size):
    # Create row and col to traverse rows and columns
    row, col = 0, 0

    boundary = size - 1
    sizeLeft = size - 1
    flag = 1

    # Variable to determine the movement
    # r = right, l = left, d = down, u = upper
    move = "r"

    # Array for matrix
    matrix = [[0 for j in range(size)] for i in range(size)]

    for i in range(1, size * size + 1):
        # Assign the value
        matrix[row][col] = size * size - i + 1

        # switch-case to determine the next index
        if move == "r":
            col += 1
        elif move == "l":
            col -= 1
        elif move == "u":
            row -= 1
        elif move == "d":
            row += 1

        # Check if the matrix has reached array boundary
        if i == boundary:
            # Add the left size for the next boundary
            boundary += sizeLeft

            # If 2 rotations have been made,
            # decrease the size left by 1
            if flag != 2:
                flag = 2
            else:
                flag = 1
                sizeLeft -= 1

            # switch-case to rotate the movement
            if move == "r":
                move = "d"
            elif move == "d":
                move = "l"
            elif move == "l":
                move = "u"
            elif move == "u":
                move = "r"

    return matrix


if __name__ == "__main__":
    # Driver Code
    size = 32

    matrix = gen_spiral(size)
    # Print the matrix
    for row in range(size):
        for col in range(size):
            n = matrix[row][col]
            print(f"{n: <5}", end="")
        print()
