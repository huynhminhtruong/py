import math
import functools as ft
from fractions import Fraction
from operator import itemgetter

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [[int(i) for i in input().split()] for _ in range(n)]
    k = int(input())
    a.sort(key=itemgetter(k))
    print("\n".join(" ".join(str(i) for i in c) for c in a))