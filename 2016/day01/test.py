with open("./input.txt", "r") as file:
    DATA = file.read().strip().split(", ")

current_direction = 0
distances = [0] * 4

for data in DATA:
    if data[0] == "R":
        current_direction += 1
    else:
        current_direction += -1

    current_direction %= 4

    distance_walked = int(data[1:])
    distances[current_direction] += distance_walked

print(abs(distances[0] - distances[2]) + abs(distances[1] - distances[3]))
