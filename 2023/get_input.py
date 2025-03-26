import subprocess
import sys

SESSION = open(".cookie", "r").read().strip()
YEAR = sys.path[0].split("/")[-1]


def get_input(day: int):
    subprocess.run(
        [
            "curl",
            f"https://adventofcode.com/{YEAR}/day/{day}/input",
            "--cookie",
            f"session={SESSION}",
            "-o",
            f"input/day{day:02d}.txt",
        ]
    )


if len(sys.argv) == 1:
    days = input("Type 'all' or numbers ranging from 1 to 25\n").split()
else:
    days = sys.argv[1:]

if "all" in days:
    for day in range(25):
        get_input(day)
else:
    for pot_day in days:
        try:
            day = int(pot_day)
            if 1 <= day <= 25:
                get_input(day)
        except ValueError:
            continue
