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

    n, a = N(), Y()
    l, v, r = 0, a[0], 1
    MIN = 2 ** 31 + 1

    for i in range(1, n):
        if a[i] < a[l]:
            if v > a[i]:
                v = a[i]
            if MIN > v - a[l]:
                MIN = v - a[l]
        else:
            r += 1
            l = i
            v = a[i]
    print(MIN if r < n else 0)
