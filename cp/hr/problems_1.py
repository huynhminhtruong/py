import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter
from collections import Counter, defaultdict, namedtuple
from itertools import combinations, groupby

def hr_1():
    n = int(input())
    a = [chr(97 + c) for c in range(0, n)]

    for i in range(2 * n - 1):
        u = a[::-1][:(i % n + 1)] if i < n else a[(i % n + 1):][::-1]
        u.extend(u[::-1][1:])
        l = "".join(["-"] * ((4 * n - 3 - (2 * len(u) - 1))//2))
        print("%s%s%s" % (l, "-".join(u), l))

def hr_minion_game():
    s = input()
    l, r, n = 0, 0, len(s)

    for i, c in enumerate(s):
        if "AEIOU".find(c) >= 0: l += n - i
        else: r += n - i
    if l > r:
        print("Kevin", l)
    elif r > l:
        print("Stuart", r)
    else:
        print("Draw")

def hr_itertools_groupby():
    s = input()
    a, l = zip(s, s), list()
    for k, g in groupby(a, lambda x: x[0]):
        l.append((len(list(g)), int(k)))
    print(*l)

def hr_collections_defaultdict():
    n, m = map(int, input().split())
    df = defaultdict(list)

    for i in range(n):
        df[input()].append(i + 1)
    for i in range(m):
        s = " ".join(str(c) for c in df[input()])
        print([s, -1][not len(s)])

def hr_collections_namedtuple():
    n, col, std = int(input()), input().split().index("MARKS"), namedtuple("std", "x")
    print("%.2f" % (sum(c.x for c in [std(int(input().split()[col])) for _ in range(n)]) / n))

if __name__ == '__main__':
    n = int(input())