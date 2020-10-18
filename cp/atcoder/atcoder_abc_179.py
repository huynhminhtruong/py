import math
import os
import random
import re
import sys

def task_A(s: str):
    last_val = s[len(s) - 1]
    s += 's' if (last_val != 's') else 'es'
    print(s)

if __name__ == "__main__":
    n, f, res = int(input()), False, 0

    for _ in range(0, n):
        d_1, d_2 = list(map(int, input().rstrip().split()))
        if not f and res >= 3:
            f = True
        if d_1 == d_2:
            res += 1
        else:
            res = 0

    print("Yes" if f or res >= 3 else "No")