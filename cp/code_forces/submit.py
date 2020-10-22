import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter

if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    d = dict()

    for i in range(m):
        s = input()
        if d.get(s) is None:
            d[s] = 0
        else:
            d[s] += 1

    a.sort()
    sorted_d = { k: v for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True) }
