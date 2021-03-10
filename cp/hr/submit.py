import math
import functools as ft
import re
from email.utils import parseaddr, formataddr
from fractions import Fraction
from operator import itemgetter
from collections import deque, Counter
from itertools import permutations, combinations, product

if __name__ == '__main__':
    s, n = input().split()
    s = sorted(s)
    d = ft.reduce(lambda x, y: x + y, [list(combinations(s, i)) for i in range(1, int(n) + 1)])
    d = "\n".join(sorted(["".join(i for i in c) for c in d], key=lambda x: (len(x), x)))
    print(d)