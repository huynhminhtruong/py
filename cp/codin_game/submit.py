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

"""
16 14
F  E  D  C  B  A
|  |--|  |  |  |
|--|  |--|  |--|
|  |--|  |--|  |
|  |  |  |  |--|
|  |--|  |--|  |
|  |  |--|  |  |
|  |  |--|  |--|
|--|  |  |--|  |
|  |  |--|  |  |
|--|  |  |  |--|
|  |--|  |  |  |
|  |  |--|  |  |
0  1  2  3  4  5
"""