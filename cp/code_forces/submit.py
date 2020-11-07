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

    n = N()
    MIN, MAX = 10 ** 9 + 1, 0
    a, f = list(), False
    for i in range(n):
        l, r = map(int, input().split())
        MIN = min(l, MIN)
        MAX = max(r, MAX)
        a.append((l, r))
    for i in range(n):
        if a[i][0] == MIN and a[i][1] == MAX:
            f = True
            break
    print(i + 1 if f else -1)