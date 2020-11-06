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
    even, odd = list(), list()

    n = N()
    a = Y()
    a.sort()

    for _ in a:
        even.append(_) if _ % 2 == 0 else odd.append(_)
    while len(even) and len(odd):
        even.pop()
        odd.pop()
    if len(even):
        even.pop()
    if len(odd):
        odd.pop()
    print("{}".format(sum(even) + sum(odd)))