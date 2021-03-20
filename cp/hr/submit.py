import math
import functools as ft
import re
from email.utils import parseaddr, formataddr
from fractions import Fraction
from operator import itemgetter
from collections import deque, Counter
from itertools import permutations, combinations, product

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    # a = mapping(convert, l)
    # print(*sorted(a), sep="\n")
    sort_phone(l)