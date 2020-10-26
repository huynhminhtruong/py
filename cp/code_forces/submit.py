import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter

if __name__ == '__main__':
    n, m, k = list(map(int, input().strip().split()))
    a, b, i = list(map(int, input().strip().split())), 0, 0

    a.sort(reverse=True)

    if m <= k:
        print(b)
    else:
        while i < len(a):
            if m <= k:
                break
            if k > 0:
                k -= 1
            elif m > 0:
                m += 1
            m -= a[i]
            b += 1
            i += 1
        print("-1" if m > k else "{}".format(b))


# 3 5 3
# 3 1 2

# 4 7 2
# 3 3 2 4

# 5 5 1
# 1 3 1 2 1

# 5 5 5
# 1 3 1 2 1

# 5 1 5
# 1 3 1 2 1

# 5 10 1
# 4 3 4 2 4

# 5 50 6
# 2 1 3 1 3
# -1