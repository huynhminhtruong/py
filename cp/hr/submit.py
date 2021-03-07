import math
import functools as ft
import re
from email.utils import parseaddr, formataddr
from fractions import Fraction
from operator import itemgetter
from collections import deque, Counter
from itertools import permutations

if __name__ == '__main__':
    s, n = input().split()
    a = sorted(list(permutations(s, int(n))), key=[itemgetter(0), lambda x: (x[0], x[1])][int(n) != 1])
    print("\n".join("".join(p) for p in a))