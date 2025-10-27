with open("./input.txt", "r") as file:
    data = file.read().strip().splitlines()


def pos(m):
    a, b, c = sorted(map(int, m))
    if a + b > c:
        return 1
    return 0


possible = 0
lists = [[], [], []]
for dat in data:
    items = sorted(map(int, dat.split()))
    for i, ite in enumerate(items):
        lists[i].append(ite)

    if len(lists[0]) == 3:
        for li in lists:
            possible += pos(li)
        lists[0] = []
        lists[1] = []
        lists[2] = []


print(possible)
