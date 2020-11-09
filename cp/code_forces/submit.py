import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter
from collections import Counter

if __name__ == '__main__':
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    n, k = P()
    a, r = list(), 0

    for i in range(n):
        p, t = P()
        a.append((p, -t))
    a.sort(key=lambda item: (item[0], item[1]), reverse=True)
    b = Counter(a)
    b = b.values()
    for i in b:
        r += i
        if k <= r:
            print(i)
            break