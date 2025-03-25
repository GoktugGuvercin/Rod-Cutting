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


def bottom_up_cut_rod(n: int, p: dict):

    revs = [0] + [-sys.maxsize for _ in range(1, n + 1)]

    # going from smaller rods to larger rods (bottom-up)
    # j is a specific value of n
    for j in range(1, n + 1):
        rev = -sys.maxsize
        for i in range(1, j + 1):  # max(p0 + rj, p1 + rj-1, ...)
            rev = max(rev, p[i] + revs[j - i])

        revs[j] = rev
    return revs[n]
