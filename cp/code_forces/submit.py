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

    n, k = P()
    a = Y()
    nxt, mx = 0, 0