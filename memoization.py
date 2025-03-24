import sys


def memoized_cut_rod(n: int, p: dict):

    r = [-sys.maxsize for _ in range(n + 1)]
    return memoized_cut_rod_aux(n, p, r)


def memoized_cut_rod_aux(n: int, p: dict, r: list):

    if r[n] >= 0:
        return r[n]

    if n == 0:
        rev = 0
    else:
        rev = -sys.maxsize
        for i in range(1, n + 1):
            rev = max(rev, p[i] + memoized_cut_rod_aux(n - i, p, r))

    r[n] = rev
    return rev
