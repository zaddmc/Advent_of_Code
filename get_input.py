import subprocess
import sys

SESSION = sys.argv[1]
YEAR = sys.argv[2]


def get_input(day: int):
    subprocess.run(
        [
            "curl",
            f"https://adventofcode.com/{YEAR}/day/{day}/input",
            "--cookie",
            f"session={SESSION}",
            "-o",
            f"{YEAR}/input/day{day:02d}.txt",
        ]
    )


def get_input_v2(day: int):
    subprocess.run(
        [
            "curl",
            f"https://adventofcode.com/{YEAR}/day/{day}/input",
            "--cookie",
            f"session={SESSION}",
            "--create-dirs",
            "-o",
            f"{YEAR}/day{day:02d}/input.txt",
        ]
    )


for day in range(25):
    get_input_v2(day + 1)
