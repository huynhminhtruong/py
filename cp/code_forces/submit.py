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

    while k > 0 and m > k and i < len(a):
        m -= a[i]
        k -= 1
        b += 1
        i += 1

    if k <= 0 and m > 0:
        print(-1)
    else:
        print(b)


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
