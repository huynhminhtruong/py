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

    n = N()
    a = Y()
    f, cnt = 0, 0
    
    for i in a:
        if i:
            cnt += 1
            f = 1
        else:
            if f:
                cnt += 1
            f = 0
    print(cnt if (a[n - 1] or not cnt) else cnt - 1)