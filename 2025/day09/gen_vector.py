from itertools import pairwise


def generate(points):
    points = [tuple(map(int, t.split(","))) for t in points]
    for p1, p2 in pairwise(points):
        yield f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" style="stroke:red;stroke-width:10"/>\n'


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    res = generate(DATA)

    with open("input.svg", "w") as file:
        file.write('<svg height="100000" width="100000">\n')
        file.writelines(res)
        file.write("</svg>\n")
