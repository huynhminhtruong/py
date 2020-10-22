import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter

if __name__ == '__main__':
    n = int(input())
    s = sorted(set(map(int, input().strip().split())))
    r = 0

    for i in range(1, len(s)):
        if r == 2:
            break
        if s[i] - s[i - 1] == 1:
            r += 1
        else:
            r = 0
    print("YES" if r == 2 else "NO")
