import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter
from collections import Counter

if __name__ == '__main__':
    m = int(input())
    b = list(map(int, input().split()))
    s = sorted(set(b))
    d = dict()
    r = []
