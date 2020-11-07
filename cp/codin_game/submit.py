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
    a.sort()
    i = 0

    if n > 0:
        while i < n and a[i] <= 0:
            i += 1
        if i == 0:
            print(a[0])
        elif i == n:
            print(a[n - 1])
        else:
            print(a[i] if a[i] <= a[i - 1] * -1 else a[i - 1])
    else:
        print(0)
