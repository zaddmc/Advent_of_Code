from itertools import pairwise


def generate(points):
    points = [tuple(map(int, t.split(","))) for t in points]
    for p1, p2 in pairwise(points):
        string = f'<line x1="{p1[0]}" y1="{p2[0]}" x2="{p1[1]}" y2="{p2[1]}" style="stroke:black;stroke-width:5" />'
        print(string)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    res = generate(DATA)
