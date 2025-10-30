def solve(data):
    childs = set()
    all_nodes = set()
    for dat in data:
        if ">" in dat:
            for child in dat.split(">")[1].strip().split(", "):
                childs.add(child)
        all_nodes.add(dat.split(" ")[0])

    return all_nodes.difference(childs).pop()


if __name__ == "__main__":

    with open("exp.txt", "r") as file:
        DATA = file.read().strip().splitlines()
        assert solve(DATA) == "tknk"

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
        print(solve(DATA))
