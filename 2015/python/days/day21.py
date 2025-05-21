import re


def solve() -> tuple[int, int]:
    get_data()

    p1 = min(adventure(True))
    p2 = max(adventure(False))
    return (p1, p2)


def adventure(goal: bool):
    for weapon in SHOP[0]:
        for armor in SHOP[1]:
            for ring1 in SHOP[2]:
                for ring2 in SHOP[2]:
                    if ring1 == ring2:
                        continue
                    result = simulate(weapon, armor, ring1, ring2)
                    cost = (
                        int(weapon[1]) + int(armor[1]) + int(ring1[1]) + int(ring2[1])
                    )
                    if goal and result:
                        yield cost
                    if not goal and not result:
                        yield cost


def simulate(weapon, armor, ring1, ring2):
    boss = BOSS.copy()
    player = {
        "Hit Points": 100,
        "Damage": int(weapon[2]) + int(ring1[2]) + int(ring2[2]),
        "Armor": int(armor[3]) + int(ring1[3]) + int(ring2[3]),
    }

    while True:
        boss["Hit Points"] -= (
            (player["Damage"] - boss["Armor"])
            if (player["Damage"] - boss["Armor"]) > 0
            else 1
        )
        if boss["Hit Points"] <= 0:
            return True

        player["Hit Points"] -= (
            (boss["Damage"] - player["Armor"])
            if (boss["Damage"] - player["Armor"]) > 0
            else 1
        )
        if player["Hit Points"] <= 0:
            return False


def get_data():
    global BOSS, SHOP
    with open("../../input/day21.txt", "r") as file:
        boss_data = file.read().splitlines()
    with open("../../input/day21.shop.txt", "r") as file:
        shop_data = map(lambda s: s.splitlines()[1:], file.read().split("\n\n"))
    SHOP = [
        [re.findall(r"(\w+)\s+(\d+)\s+(\d+)\s+(\d+)", s)[0] for s in data]
        for data in shop_data
    ]

    BOSS = {s.split(": ")[0]: int(s.split(": ")[1]) for s in boss_data}


if __name__ == "__main__":
    print(solve())
