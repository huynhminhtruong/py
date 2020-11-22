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
    a = Y()
    l, r, down, MAX = 0, 1, False, 0

    for i in range(1, n):
        if a[i] > a[i - 1]:
            if not down:
                r += 1
            else:
                if r > MAX:
                    MAX = r
                r = i - l + 1
                down = False
        else:
            if a[i] < a[i - 1]:
                l = i
            r += 1
            down = True
    print(r if r > MAX else MAX)