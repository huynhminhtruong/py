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
    a, b = Y(), list()

    for i in range(1, n):
        if a[i] == 1:
            b.append(a[i - 1])
    b.append(a[-1])
    print("{0}\n{1}".format(len(b), " ".join([str(x) for x in b])))