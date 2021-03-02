from itertools import groupby
from collections import defaultdict, namedtuple

if __name__ == '__main__':
    n, col, std = int(input()), input().split().index("MARKS"), namedtuple("std", "x")
    print("%.2f" % (sum(c.x for c in [std(int(input().split()[col])) for _ in range(n)]) / n))