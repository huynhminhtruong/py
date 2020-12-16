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
    a = Y()
    r, s, mx = 0, 0, 0
    for _ in a:
        if _ < 0:
            s += 1
        else:
            r += 1
    for i in range(k):
        mx = max(abs((s - a[i::k].count(-1)) - (r - a[i::k].count(1))), mx)
    print(mx)