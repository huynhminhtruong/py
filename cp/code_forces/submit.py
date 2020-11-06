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

    n, m = Y()
    a, r = list(), 0

    for i in range(m):
        a.append(Y())
    a.sort(key=itemgetter(1), reverse=True)

    for i in a:
        if n <= 0:
            break
        h = n - i[0]
        r += i[0] * i[1] if h > 0 else n * i[1]
        n -= i[0]

    print(r)
