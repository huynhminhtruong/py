import math
import functools as ft
import re
from fractions import Fraction
from operator import itemgetter
from collections import deque

if __name__ == '__main__':
    n = int(input())
    regex = "[#]+[a-fA-F0-9]{3,6}"
    a, f = list(), False
    for i in range(n):
        t = input()
        if t.count("{") > 0 or t.count("}") > 0:
            f = not f
        elif f:
            a.extend(filter(lambda x: 4 <= len(x) < 9, re.findall(regex, t)))
    print("\n".join(a))