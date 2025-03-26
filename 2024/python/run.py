from days import *

for day in range(25):
    try:
        exec(f"print(day{1 + day:02d}.solve())")
    except Exception as e:
        print(e)
