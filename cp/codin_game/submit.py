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

    l = N()
    h = N()
    s = [ord(x.upper()) for x in input()]
    t, res = list(), list()

    for i in range(h):
        t.append(input())
    for row in t:
        r = ""
        for i in range(len(s)):
            if s[i] >= ord('A') and s[i] <= ord('Z'):
                p = (s[i] % ord('A')) * l
                r += row[p:p + l]
            else:
                r += row[l * 26:l * 27]
        res.append(r)
    for row in res:
        print(row)