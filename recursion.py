import sys


def cut_rod(n: int, p: dict) -> int:

    if n == 0:
        return 0

    rev = -sys.maxsize
    for i in range(1, n + 1):
        rev = max(rev, p[i] + cut_rod(n - i, p))

    return rev
