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


def isValid(original, return_fail=False):
    """no"""
    is_valid_check_list = []
    for check in original:
        if True not in [tval in is_valid_check_list for tval in orderdict[check]]:
            is_valid_check_list.append(check)
        else:
            if return_fail:
                return check
            return False
    return True


def fix(original):
    """no"""
    work_list = []
    for val in original:
        for new_index in range(len(work_list) + 1):
            work_list.insert(new_index, val)
            if isValid(work_list):
                break
            work_list.remove(val)
    if not isValid(work_list):
        raise ValueError("Not good")
    return int(work_list[int(len(work_list) / 2)])


sum_val_valid = 0
sum_val_invalid = 0
for line in checklist:
    original_list = line[:-1].split(",")
    if isValid(original_list):
        sum_val_valid += int(original_list[int(len(original_list) / 2)])
    else:
        sum_val_invalid += fix(original_list)


print(f"Final value for valid {sum_val_valid}")
print(f"Final value for invalid {sum_val_invalid}")
