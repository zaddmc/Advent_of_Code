import random
from itertools import cycle


def solve(player_stats, boss_stats, hard_mode):
    best = 10000000000
    for _ in range(500_000):
        res = simulate(player_stats, boss_stats, best, hard_mode)
        if res and res < best:
            best = res
    return best


def simulate(player_stats, boss_stats, best_score, hard_mode):
    boss = {"Hit Points": boss_stats[0], "Damage": boss_stats[1]}
    player = {"Hit Points": player_stats[0], "Mana": player_stats[1]}
    effects = {"Shield": 0, "Poison": 0, "Recharge": 0}
    mana_spent = 0

    for i, turn in enumerate(cycle(("player", "boss"))):
        if hard_mode:
            player["Hit Points"] -= 1
            if player["Hit Points"] <= 0:
                return None

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
                effects[name] -= 1 if turns else 0

        if boss["Hit Points"] <= 0:
            return mana_spent

        if turn == "player":
            while True:
                match random.choice(
                    ["Magic Missile", "Drain", "Shield", "Poison", "Recharge"]
                ):
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
                    case x:
                        print("failed", x)

        if best_score < mana_spent:
            return None

        if boss["Hit Points"] <= 0:
            return mana_spent

        if turn == "boss":
            dam = boss["Damage"] if not effects["Shield"] else boss["Damage"] - 7
            player["Hit Points"] -= dam if dam > 1 else 1

            if player["Hit Points"] <= 0:
                return None


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        boss_stats = tuple(
            map(lambda s: int(s.split(": ")[1]), file.read().splitlines())
        )
    player_stats = (50, 500)
    p1 = solve(player_stats, boss_stats, False)
    p2 = solve(player_stats, boss_stats, True)

    print(p1, p2)
