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


def isValid(original):
    """no"""
    is_valid_check_list = []
    for check in original:
        if True not in [tval in is_valid_check_list for tval in orderdict[check]]:
            is_valid_check_list.append(check)
        else:
            return False
    return True


sum_val_valid = 0
for line in checklist:
    original_list = line[:-1].split(",")
    if isValid(original_list):
        sum_val_valid += int(original_list[int(len(original_list) / 2)])

print(f"Final value {sum_val_valid}")
print(
    "Should be false : "
    + str(isValid(["52", "23", "24", "83", "51", "56", "37", "48", "96", "88", "63"]))
)
print("Should be True  : " + str(isValid(["73", "56", "42", "27", "18", "97", "53"])))
