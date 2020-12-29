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

    a, b = P()
    cnt, l = 0, [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    n = str(list(range(a, b + 1)))
    
    for i in range(10):
        cnt += l[i] * n.count(str(i))
    print(cnt)