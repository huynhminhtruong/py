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
    H, V = dict(), dict()
    r = ""

    n *= n

    for i in range(n):
        h, v = P()
        if not (h in H.keys() or v in V.keys()):
            H[h] = H.get(h, True)
            V[v] = V.get(v, True)
            r += str(i + 1) + " "
    print(r.strip())