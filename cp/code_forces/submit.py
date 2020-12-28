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
    f, i, j = 0, 0, n - 1

    while i < n - 1 and a[i] < a[i + 1]:
        i += 1
    while j > 0 and a[j] < a[j - 1]:
        j -= 1
    f = (j - i + 1 == a[i:j+1].count(a[i]))
    print("YNEOS"[not f::2])