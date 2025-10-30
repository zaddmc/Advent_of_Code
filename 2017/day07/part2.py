def solve(data):
    childs = set()
    all_nodes = set()
    quic_dict = {}
    for dat in data:
        source_name = dat.split(" ")[0]
        source_weight = int(dat.split(" ")[1].strip("()"))
        all_nodes.add(source_name)

        if ">" in dat:
            asd = dat.split(">")[1].strip().split(", ")
            for child in asd:
                childs.add(child)
            quic_dict[source_name] = (source_weight, tuple(asd))

        else:
            quic_dict[source_name] = (source_weight, None)

    root_name = all_nodes.difference(childs).pop()
    root_node = TreeNode(*quic_dict[root_name], quic_dict)
    return root_node.find_error()[1]


def is_same(li: list[int]):
    nli = sorted(li)

    if nli[0] == nli[-1]:
        return True
    else:
        if nli.count(nli[0]) < nli.count(nli[-1]):
            return nli[-1] - nli[0], nli[0]
        else:
            return nli[0] - nli[-1], nli[-1]


class TreeNode:
    def __init__(self, weight, nodes, ndict):
        self.original_weight = weight
        self.nodes = list(nodes) if nodes else []

        for idx, node in enumerate(self.nodes):
            self.nodes[idx] = TreeNode(*ndict[node], ndict)

    def find_error(self):
        if len(self.nodes) == 0:
            return self.original_weight

        vals = [node.find_error() for node in self.nodes]
        for l in vals:
            if isinstance(l, tuple):
                return l

        res = is_same(vals)
        if not isinstance(res, bool):
            return True, self.nodes[vals.index(res[1])].original_weight + res[0]

        return sum(vals) + self.original_weight

    def __str__(self):
        if len(self.nodes) == 0:
            return str(self.original_weight)
        return f"{self.original_weight=}  {self.nodes=}"

    def __repr__(self):
        if len(self.nodes) == 0:
            return str(self.original_weight)
        return f"{self.original_weight=}  {self.nodes=}"


if __name__ == "__main__":
    with open("exp.txt", "r") as file:
        DATA = file.read().strip().splitlines()
        assert solve(DATA) == 60

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
        print(solve(DATA))
