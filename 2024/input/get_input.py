import subprocess

for day in range(1, 25):
    subprocess.run(
        [
            "curl",
            f"https://adventofcode.com/2024/day/{day}/input",
            "--cookie",
            "session=53616c7465645f5fe90e845c7b0a28bc2f7106c600c7af38cca0a46bed8c716732cffdd2d570d60ea38e9a61c6c01fef88099e979d66f96b0d9d12de2315e95a",
            "-o",
            f"day{day}.txt",
        ]
    )
