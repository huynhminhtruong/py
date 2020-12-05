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

    n, v = P()
    r = list()

    for i in range(n):
        a = Y()
        m = min(a[1:])
        if v > m:
            r.append(i + 1)
    print("{0}".format(len(r)))
    print(*r)