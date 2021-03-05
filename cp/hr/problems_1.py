import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter
from collections import Counter, defaultdict, namedtuple, OrderedDict as od, deque
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

def hr_collections_ordereddict():
    n = int(input())
    d = od()

    for i in range(n):
        a = input().split()
        l = len(a)
        key = " ".join(a[i] for i in range(l - 1))
        d[key] = d.get(key, 0) + int(a[l - 1])
    for k, v in d.items():
        print(k, v)

def hr_count_words():
    n = int(input())
    d = od()

    for i in range(n):
        word = input()
        d[word] = d.get(word, 0) + 1
    print("%d\n%s" % (len(d.items()), " ".join(str(i) for i in d.values())))

def hr_collections_deque():
    n = int(input())
    d, p = deque(), ["append", "pop", "popleft", "appendleft"]

    for i in range(n):
        a = input().split()

        if len(a) > 1:
            if p.index(a[0]) == 0: d.append(a[1])
            else: d.appendleft(a[1])
        else:
            if p.index(a[0]) == 1: d.pop()
            else: d.popleft()
    print(*d)

def hr_reduce_fraction():
    n = int(input())
    a = [Fraction(*[int(i) for i in input().split()]) for _ in range(n)]
    r = ft.reduce(lambda x, y: x * y, a)
    print(r.numerator, r.denominator)

def hr_sort_itemgetter():
    n, m = map(int, input().split())
    a = [[int(i) for i in input().split()] for _ in range(n)]
    k = int(input())
    a.sort(key=itemgetter(k))
    print("\n".join(" ".join(str(i) for i in c) for c in a))

def hr_regex():
    n = int(input())
    regex = "[#]+[a-fA-F0-9]{3,6}"
    a, f = list(), False
    for i in range(n):
        t = input()
        if t.count("{") > 0 or t.count("}") > 0:
            f = not f
        elif f:
            a.extend(filter(lambda x: 4 <= len(x) < 9, re.findall(regex, t)))
    print("\n".join(a))

if __name__ == '__main__':
    n = int(input())