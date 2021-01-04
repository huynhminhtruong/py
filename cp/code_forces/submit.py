import math
import os
import random
import re
import sys
import functools
import datetime as dt
from operator import itemgetter, attrgetter
from collections import Counter

if __name__ == '__main__':
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    a = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    c = input()
    n = input()
    print("YNEOS"[not ((a.index(n) - a.index(c) + 7) % 7 in (0, 2, 3))::2])