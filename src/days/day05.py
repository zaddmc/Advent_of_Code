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

orderdict = {}
for rule in orderrules:
    lhs, rhs = rule[:-1].split("|")
    try:
        orderdict[lhs].append(rhs)
    except:
        orderdict[lhs] = [rhs]

sum_val = 0
for line in checklist:
    list_val = []
    original_list = line[:-1].split(",")
    for val in original_list:
        if True not in [tval in list_val for tval in orderdict[val]]:
            list_val.append(val)
    print(f"Original list {original_list}")
    print(f"Detemined val {list_val}")
    valid = len(original_list) == len(list_val)
    print(f"Is valid {valid}")
    if valid:
        sum_val += int(list_val[int(len(list_val) / 2)])

print(f"Final value {sum_val}")
