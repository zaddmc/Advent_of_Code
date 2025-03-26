import subprocess


def duplication(day: int):
    subprocess.run(
        [
            "cp",
            "./days/day01.py",
            f"./days/day{day:02d}.py",
        ]
    )


for day in range(24):
    duplication(day + 2)
