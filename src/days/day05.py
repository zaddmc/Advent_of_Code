"""No"""

orderrules = []
checklist = []
# pylint: disable-msg=C0103
with open("../../input/day5.txt", "r", encoding="utf-8") as source:
    flag = False
    for line in source.readlines():
        if line == "\n":
            flag = True
            continue
        if flag:
            checklist.append(line)
        else:
            orderrules.append(line)

orderlist = []
for rule in orderrules:
    lhs, rhs = rule[:-1].split("|")

    if lhs not in orderlist and rhs not in orderlist:
        orderlist.append(lhs)
        orderlist.append(rhs)
        continue

    if lhs in orderlist and rhs not in orderlist:
        orderlist.insert(orderlist.index(lhs) + 1, rhs)

    print(f"Failed to allocate either {lhs} or {rhs}")

print(orderlist)
