import random
from itertools import cycle, permutations


def solve() -> tuple[int, int]:
    get_data()
    global BEST
    BEST = 1203123123123123123123123123
    actions = [
        "Recharge",
        "Shield",
        "Recharge",
        "Shield",
        "Drain",
        "Poison",
        "Poison",
        "Poison",
        "Magic Missile",
        "Magic Missile",
    ]
    for action in permutations(actions):
        result = simulate(action)
        if result and result < BEST:
            BEST = result
            print(result, action)
    exit()
    p1 = adventure()
    return (p1, -1)


def adventure():
    global BEST
    BEST = 100000000000
    for _ in range(500_000):
        result = simulate()
        if result and result < BEST:
            print("new best", result)
            BEST = result

    return BEST


def simulate(actions):
    boss = BOSS.copy()
    # boss = {"Hit Points": 14, "Damage": 8}
    player = {"Hit Points": 50, "Mana": 500}
    effects = {n: 0 for n in ["Shield", "Poison", "Recharge"]}
    mana_spent = 0
    actions = cycle(actions)

    for i, turn in enumerate(cycle(("player", "boss"))):
        for name, turns in effects.items():
            match name:
                case "Poison":
                    if turns:
                        boss["Hit Points"] -= 3
                        if boss["Hit Points"] <= 0:
                            return mana_spent
                case "Recharge":
                    if turns:
                        player["Mana"] += 101
            if turns:
                effects[name] -= 1 if turns > 0 else 0

        if turn == "player":
            while True:
                match actions.__next__():
                    # match random.choice(
                    #    ["Magic Missile", "Drain", "Shield", "Poison", "Recharge"]
                    # ):
                    case "Magic Missile":
                        if player["Mana"] >= 53:
                            player["Mana"] -= 53
                            mana_spent += 53
                            boss["Hit Points"] -= 4
                            break
                        return None
                    case "Drain":
                        if player["Mana"] >= 73:
                            player["Mana"] -= 73
                            mana_spent += 73
                            boss["Hit Points"] -= 2
                            player["Hit Points"] += 2
                            break
                    case "Shield":
                        if player["Mana"] >= 113 and not effects["Shield"]:
                            player["Mana"] -= 113
                            mana_spent += 113
                            effects["Shield"] = 6
                            break
                    case "Poison":
                        if player["Mana"] >= 173 and not effects["Poison"]:
                            player["Mana"] -= 173
                            mana_spent += 173
                            effects["Poison"] = 6
                            break
                    case "Recharge":
                        if player["Mana"] >= 229 and not effects["Recharge"]:
                            player["Mana"] -= 229
                            mana_spent += 229
                            effects["Recharge"] = 5
                            break

        if boss["Hit Points"] <= 0:
            return mana_spent

        if mana_spent > BEST:
            return None

        if turn == "boss":
            player["Hit Points"] -= boss["Damage"] - 7 if effects["Shield"] else 0

            if player["Hit Points"] <= 0:
                return None


def get_data():
    global BOSS
    with open("../../input/day22.txt", "r") as file:
        data = file.read().splitlines()
    BOSS = {s.split(": ")[0]: int(s.split(": ")[1]) for s in data}


if __name__ == "__main__":
    print(solve())
