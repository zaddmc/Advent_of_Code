with open("./input.txt", "r") as file:
    data = file.read().strip().splitlines()

possible = 0
for dat in data:
    a, b, c = sorted(map(int, dat.split()))
    if a + b > c:
        possible += 1


print(possible)
