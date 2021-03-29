import math
import functools as ft
import re
from email.utils import parseaddr, formataddr
from fractions import Fraction
from operator import itemgetter
from collections import deque, Counter
from itertools import permutations, combinations, product

if __name__ == '__main__':
    a = set(input().split())
    n, ans = int(input()), True

    while n > 0:
        b = set(input().split())
        k = len(b & a)
        ans = (k == len(b) and k < len(a)) and ans
        n -= 1
    print(ans)