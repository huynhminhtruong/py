import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter

if __name__ == '__main__':
    n = int(input())
    a, b, c = list(map(int, input().strip().split()))

    a.sort()

    # tmp = set('apple')
    # print(tmp)

# 5
# 1 2 3 4 5
# Expected
# 5
# 5 4 3 2 1

# 6
# 1 1 2 2 3 3
# Expected
# 5
# 1 2 3 2 1

# 1 1 2 2 3 4 5
# 1 2 5 4 3 2 1