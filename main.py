import sys


def cut_rod(n: int, p: dict) -> int:

    if n == 0:
        return 0

    rev = -sys.maxsize
    for i in range(1, n + 1):
        rev = max(rev, p[i] + cut_rod(n - i, p))

    return rev


lengths = [i for i in range(1, 11)]
prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
price_dict = {le: p for le, p in zip(lengths, prices)}

for i in range(1, 11):
    print(f"Length {i}, max revenue: ", cut_rod(i, price_dict))
