import json


def solve() -> tuple[int, int]:
    get_data()
    p1 = sum(find_number(DATA, False))
    p2 = sum(find_number(DATA, True))
    return (p1, p2)


def find_number(segment, er: bool):
    if isinstance(segment, list):
        for s in segment:
            yield from find_number(s, er)
        return

    if isinstance(segment, dict):
        if er and any([True for s in segment.values() if s == "red"]):
            return
        for s in segment.values():
            yield from find_number(s, er)
        return

    if isinstance(segment, int):
        yield segment
        return

    if isinstance(segment, str):
        return

    print("Unhandled type:", type(segment))


def get_data():
    global DATA
    with open("../../input/day12.txt", "r") as file:
        DATA = json.loads(file.read().strip())


if __name__ == "__main__":
    print(solve())
