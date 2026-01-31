import re


def solve(ips):
    counter = 0
    for ip in ips:
        if aba_filter(ip):
            counter += 1
    return counter


def aba_filter(string: str):
    hyper = False
    aba = set()
    bab = set()
    for i in range(len(string) - 2):
        if string[i] == "[":
            hyper = True
            continue
        if string[i] == "]":
            hyper = False
            continue

        if string[i] != string[i + 1] and string[i] == string[i + 2]:
            stri = string[i + 1] + string[i] + string[i + 1]
            if hyper:
                bab.add((string[i + 1], string[i]))
            else:
                aba.add((string[i], string[i + 1]))

    for ab in aba:
        if ab in bab:
            return True


if __name__ == "__main__":

    with open("input.txt", "r") as file:
        DATA = file.read().strip().splitlines()
    print(solve(DATA))
