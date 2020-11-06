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
    N = lambda: int(input())

    n = N()
    a = Y()
    r = 0
    a = [(-a[k], k % len(a) + 1) for k in range(n)]
    a.sort()
    for i in range(n):
        r += -a[i][0] * i + 1
    print("{0}\n{1}".format(r, " ".join(map(str, [x[1] for x in a]))))